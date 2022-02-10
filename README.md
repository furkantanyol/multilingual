# multilingual

![Alt Text](https://media.giphy.com/media/TksBWToEdzfEtNymcb/giphy.gif)

This is a command line application that automatically translates the input sentence to multiple languages and adds the 
translations to respective translation json files

You must run this script in the root folder where you keep your translation files.
For now, this script assumes that you name your translations with the following patterns:
```shell
├───public  // translations root folder
│   ├───de.json  // {country-iso}.json
|   ├───main_de.json  // *_{country_iso}.json
│   └───main-de.json  // *-{country_iso}.json
```

## Installation

1. Make sure you have at least **Python v3.10.2** installed.

2. Install the package:
```shell
$ pip install multilingual
```

3. Go to the project folder where you keep your translation json files and run **multilingual** command with the sentence you want to translate:
```shell
$ cd {YOUR_PROJECT}/{TRANSLATIONS_DIR}` 

$ multilingual "Sentence to be translated"

# SENTENCE_TO_BE_TRANSLATED :  Sentence to be translated ---> en-gb.json
# SENTENCE_TO_BE_TRANSLATED :  Frase a traducir ---> es.json
# SENTENCE_TO_BE_TRANSLATED :  Phrase à traduire ---> fr.json
# SENTENCE_TO_BE_TRANSLATED :  번역 될 문장 ---> ko.json
# SENTENCE_TO_BE_TRANSLATED :  Satz, um übersetzt zu werden ---> de.json
# SENTENCE_TO_BE_TRANSLATED :  Sentence to be translated ---> en.json
# SENTENCE_TO_BE_TRANSLATED :  要翻译的句子 ---> zh.json
```

4. You can optionally specify your own key for your translation:
```shell
$ multilingual "Sentence to be translated" --key=TRANSLATION

# TRANSLATION:  Sentence to be translated ---> main-en-gb.json
# TRANSLATION:  Frase a traducir ---> main-es.json
# TRANSLATION:  Phrase à traduire ---> main-fr.json
# TRANSLATION:  번역 될 문장 ---> main-ko.json
# TRANSLATION:  Satz, um übersetzt zu werden ---> main-de.json
# TRANSLATION:  Sentence to be translated ---> main-en.json
# TRANSLATION:  要翻译的句子 ---> main-zh.json
```


## Requirements

* Python 3.10.2
