"""Module providingFunction printing python version."""
from deep_translator import MyMemoryTranslator #imports translator from package
def english_to_french(english_text): 
    """Function translating english to french"""
    translator = MyMemoryTranslator(source='english',target='french')
    french_text = translator.translate(english_text)
    return french_text
def french_to_english(french_text):     
    """Function translating french to english"""
    translator = MyMemoryTranslator(source="french",target='english')
    english_text = translator.translate(french_text)
    return english_text
