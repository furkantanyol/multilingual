import typer
import os
import re
import json
from googletrans import Translator

translator = Translator()
app = typer.Typer()

MOST_TRANSLATED_LANGUAGES = "en,de,es,fr,zh-CN,ja,ko,ar,iw,hi,ur".split(",")


@app.command()
def translate(text: str, key: str = typer.Option(None)):
    json_files = get_json_files_in_dir()

    for file_name in json_files:
        language = extract_language_from_file_name(file_name)

        if language == 'invalid':
            continue

        translation = translate_text_to_language(text, language)

        if translation == 'invalid':
            continue

        key = key or parametrize(remove_special_chars(text))

        write_to_file(file_name, key, translation)


def write_to_file(file_name: str, key: str, value: str):
    with open(file_name, "r") as file:
        data = json.load(file)  # 1. Read file

        data[key] = value  # 2. Update json object
        with open(file_name, "w") as file:  # 3. Write json file
            json.dump(data, file, sort_keys=True, ensure_ascii=False)
            typer.echo(f"{key}: {value} ---> {file_name}")


def get_json_files_in_dir() -> [str]:
    return list(filter(lambda file: file.endswith(".json"), os.listdir()))


def extract_language_from_file_name(file_name: str) -> str:
    if len(file_name) <= 0:
        return 'invalid'

    lang_json_str = re.findall('[A-Za-z]{2}.json', file_name)[0]
    lang = lang_json_str.split('.')[0]
    return validate_language(lang)


def validate_language(language: str) -> str:
    if 'gb' in language:  # british english -> english
        language = 'en'

    if 'zh' in language:  # chinese -> simplified chinese
        language = 'zh-CN'

    if language not in MOST_TRANSLATED_LANGUAGES:
        language = 'invalid'

    return language


def translate_text_to_language(text: str, language: str) -> str:
    if language == 'en':
        return text
    try:
        translation = translator.translate(text, src='en', dest=language)
        return translation.text
    except:
        return 'invalid'


def parametrize(text: str, word_count=6) -> str:
    return "_".join(text.split(" ", word_count)[:word_count]).upper()


def remove_special_chars(text: str) -> str:
    return re.sub('[^a-zA-Z0-9 \n.]', '', text)


if __name__ == "__main__":
    app()
