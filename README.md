# multilingual

This is a command line application that automatically translates the input sentence to multiple languages and adds the 
translations to respective translation json files

You must run this script in the root folder where you keep your translation files.
For now, this script assumes that you name your translations with the following patterns:
```shell
{country-iso}.json --> de.json 
*-{country_iso}.json --> main-de.json
```

![Alt Text](https://media.giphy.com/media/TksBWToEdzfEtNymcb/giphy.gif)

## Installation

* Install **python 3.10.2**

* Clone this repo: 
```shell
$ git clone https://github.com/furkantanyol/multilingual.git
```

* There are 2 ways to run this command line application:

1. Run the script file in your local directly:
```shell
# 1. Go to the project folder where you keep your translation json files: 
$ cd {YOUR_PROJECT}/{TRANSLATIONS_DIR}` 

# 2. Point to the correct directory where this project is installed and run 
$ python {CLONED_ROOT}/multilingual/multilingual.py "Sentence to be translated"
# SENTENCE_TO_BE_TRANSLATED :  Sentence to be translated ---> main-en-gb.json
# SENTENCE_TO_BE_TRANSLATED :  Frase a traducir ---> main-es.json
# SENTENCE_TO_BE_TRANSLATED :  Phrase à traduire ---> main-fr.json
# SENTENCE_TO_BE_TRANSLATED :  번역 될 문장 ---> main-ko.json
# SENTENCE_TO_BE_TRANSLATED :  Satz, um übersetzt zu werden ---> main-de.json
# SENTENCE_TO_BE_TRANSLATED :  Sentence to be translated ---> main-en.json
# SENTENCE_TO_BE_TRANSLATED :  要翻译的句子 ---> main-zh.json
```

2. Install & run the distribution in your local:
```shell
# 1. Install build tool: 
$ pip install build

# 2. In the project root, run: 
$ python -m build 
# This will result in two output files in the dist directory: 
# - dist/multilingual-0.0.1.tar.gz 
# - dist/multilingual-0.0.1-py3-none-any.whl

# 3. Install the distribution you just created:
$ pip install dist/multilingual-0.0.1-py3-none-any.whl 
# This should create the CLI shortcuts in the current Python environment’s bin directory.
# - {Python Path}/bin/my-application
# - {Python Path}/bin/another-application

# 4. Go to the project folder where you keep your translation json files: 
$ cd {YOUR_PROJECT}/{TRANSLATIONS_DIR}

# 5. Run:
$ multilingual "Sentence to be translated"
# SENTENCE_TO_BE_TRANSLATED :  Sentence to be translated ---> main-en-gb.json
# SENTENCE_TO_BE_TRANSLATED :  Frase a traducir ---> main-es.json
# SENTENCE_TO_BE_TRANSLATED :  Phrase à traduire ---> main-fr.json
# SENTENCE_TO_BE_TRANSLATED :  번역 될 문장 ---> main-ko.json
# SENTENCE_TO_BE_TRANSLATED :  Satz, um übersetzt zu werden ---> main-de.json
# SENTENCE_TO_BE_TRANSLATED :  Sentence to be translated ---> main-en.json
# SENTENCE_TO_BE_TRANSLATED :  要翻译的句子 ---> main-zh.json
```
     
* For a clean environment: 

```shell
# create virtual environment
$ python -m venv .env/fresh-install-test

# activate your virtual environment
$ . .env/fresh-install-test/bin/activate

# install your package into this fresh environment
$ pip install dist/multilingual-0.0.1-py3-none-any.whl

# your shortcuts are now in the venv bin directory
$ ls .env/fresh-install-test/bin/
multilingual

# so you can run it directly from the cli
$ multilingual "Sentence to be translated"
# SENTENCE_TO_BE_TRANSLATED :  Sentence to be translated ---> main-en-gb.json
# SENTENCE_TO_BE_TRANSLATED :  Frase a traducir ---> main-es.json
# SENTENCE_TO_BE_TRANSLATED :  Phrase à traduire ---> main-fr.json
# SENTENCE_TO_BE_TRANSLATED :  번역 될 문장 ---> main-ko.json
# SENTENCE_TO_BE_TRANSLATED :  Satz, um übersetzt zu werden ---> main-de.json
# SENTENCE_TO_BE_TRANSLATED :  Sentence to be translated ---> main-en.json
# SENTENCE_TO_BE_TRANSLATED :  要翻译的句子 ---> main-zh.json
```

You can optionally specify your own key for your translation:
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

* python 3.10.2
