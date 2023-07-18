"""imports functions to be tested"""
import unittest
from translator import english_to_french, french_to_english 

class Test_translator(unittest.TestCase): #defines a class for unit test"""
    def test_english_to_french(self):   
        """it test the veracity of the translation"""
        self.assertEqual(english_to_french('Good morning'), 'Bonjour')

    def test_french_to_english(self): 
        """it test the veracity of the translation"""
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()