import unittest

from multilingual.main import remove_special_chars, parametrize, translate_text_to_language, validate_language, \
    extract_language_from_file_name

from googletrans import Translator

translator = Translator()


class TestRemoveSpecialChars(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_special_chars(""), "")

    def test_not_to_remove_spaces(self):
        self.assertEqual(remove_special_chars(" "), " ")

    def test_to_remove_special_characters_simple(self):
        self.assertEqual(remove_special_chars("LET'S_GO"), "LETSGO")

    def test_to_remove_special_characters_complex(self):
        self.assertEqual(remove_special_chars("!#Remove $special *characters* /other/ than! digits, "
                                              "characters and spaces!!!$"),
                         "Remove special characters other than digits characters and spaces")


class TestParametrize(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(parametrize(""), "")

    def test_parametrize_one_word(self):
        self.assertEqual(parametrize("hello"), "HELLO")

    def test_parametrize_multiple_words(self):
        self.assertEqual(parametrize("this sentence needs to be parametrized"),
                         "THIS_SENTENCE_NEEDS_TO_BE_PARAMETRIZED")

    def test_parametrize_max_6_words_by_default(self):
        self.assertEqual(parametrize("this sentence needs to be parametrized quickly"),
                         "THIS_SENTENCE_NEEDS_TO_BE_PARAMETRIZED")

    def test_parametrize_specify_max_words(self):
        self.assertEqual(parametrize("this sentence needs to be parametrized quickly", 7),
                         "THIS_SENTENCE_NEEDS_TO_BE_PARAMETRIZED_QUICKLY")


class TestTranslateTextToLanguage(unittest.TestCase):

    def test_english_returns_the_text_itself(self):
        self.assertEqual(translate_text_to_language("hello", "en"), "hello")


class TestValidateLanguage(unittest.TestCase):

    def test_empty_language(self):
        self.assertEqual(validate_language(""), "invalid")

    def test_british_english(self):
        self.assertEqual(validate_language("en-gb"), "en")

    def test_chinese(self):
        self.assertEqual(validate_language("zh"), "zh-CN")

    def test_language_not_in_most_translated_languages(self):
        self.assertEqual(validate_language("tr"), "invalid")

    def test_language_in_most_translated_languages(self):
        self.assertEqual(validate_language("de"), "de")


class TestExtractLanguageFromFileName(unittest.TestCase):

    def test_empty_file_name(self):
        self.assertEqual(extract_language_from_file_name(""), 'invalid')

    def test_iso_file_names(self):
        self.assertEqual(extract_language_from_file_name("de.json"), 'de')
        self.assertEqual(extract_language_from_file_name("en-gb.json"), 'en')

    def test_dashed_file_names(self):
        self.assertEqual(extract_language_from_file_name("main-de.json"), 'de')
        self.assertEqual(extract_language_from_file_name("main-en-gb.json"), 'en')

    def test_underscored_file_names(self):
        self.assertEqual(extract_language_from_file_name("main_de.json"), 'de')
        self.assertEqual(extract_language_from_file_name("main_en-gb.json"), 'en')


if __name__ == '__main__':
    unittest.main()
