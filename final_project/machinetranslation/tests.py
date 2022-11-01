"""
Test for null input for frenchToEnglish
Test for null input for englishToFrench.
Test for the translation of the world ‘Hello’ and ‘Bonjour’.
Test for the translation of the world ‘Bonjour’ and ‘Hello’.
"""

import unittest

from translator import englishToFrench, frenchToEnglish


class TestEnglishToFrench(unittest.TestCase):
    def testNullInput(self):
        self.assertEqual(englishToFrench(""), "")

    def testTranslate(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")


class TestFrenchToEnglish(unittest.TestCase):
    def testNullInput(self):
        self.assertEqual(frenchToEnglish(""), "")

    def testTranslate(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
