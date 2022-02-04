import typer
import os
import re
import json
from googletrans import Translator

translator = Translator()
app = typer.Typer()


@app.command()
def translate(text: str):
    json_files = get_json_files_in_dir()

    for file_name in json_files:
        language = extract_language_from_file_name(file_name)

        if language == 'invalid':
            continue

        translation = translate_text_to_language(text, language)

        if translation == 'invalid':
            continue

        write_to_file(file_name, snake_case(text), translation)

def write_to_file(file_name: str, key: str, value: str):
    with open(file_name, "r") as file:
        data = json.load(file) # 1. Read file
        data[key] = value # 2. Update json object
        with open(file_name, "w") as file: # 3. Write json file
            json.dump(data, file, ensure_ascii=False)
            typer.echo(f"{key}: {value} ---> {file_name}")


def get_json_files_in_dir() -> [str]:
    return list(filter(lambda file: file.endswith(".json"), os.listdir()))


def extract_language_from_file_name(file_name: str) -> str:
    language = re.findall('-(.*)\.', file_name)[0]
    return validate_language(language)


def validate_language(language: str) -> str:
    match language:
        case 'tlh':
            return 'invalid'
        case 'en-gb':
            return 'en'
        case 'zh':
            return 'zh-CN'
    return language


def translate_text_to_language(text: str, language: str) -> str:
    if language == 'en':
        return text
    try:
        translation = translator.translate(text, src='en', dest=language)
        return translation.text
    except:
        return 'invalid'


def snake_case(s):
    return '_'.join(
        re.sub('([A-Z][a-z]+)', r' \1',
               re.sub('([A-Z]+)', r' \1',
                      s.replace('-', ' '))).split()).upper()


if __name__ == "__main__":
    app()
