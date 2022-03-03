import pandas as pd
from translate import Translator
from deep_translator import GoogleTranslator


# translator= Translator(to_lang="tr")

# def translate_it(word):
#     translation = translator.translate(word)
#     return translation


def translate_it(to_translate):
    translated = GoogleTranslator(source='auto', target='tr').translate(to_translate)
    return translated