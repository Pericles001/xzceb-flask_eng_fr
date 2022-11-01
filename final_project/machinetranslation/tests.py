"""
Test for null input for frenchToEnglish
Test for null input for englishToFrench.
Test for the translation of the world ‘Hello’ and ‘Bonjour’.
Test for the translation of the world ‘Bonjour’ and ‘Hello’.
"""

import unittest

from translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
    def testNullInput(self):
        self.assertEqual(english_to_french(""), "")

    def testTranslate(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")


class TestFrenchToEnglish(unittest.TestCase):
    def testNullInput(self):
        self.assertEqual(french_to_english(""), "")

    def testTranslate(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
