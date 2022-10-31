import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """
    Unit test class to check assertEqual for method english_to_french
    """
    def test_assert_equal(self):
        """
        Method checks for equality for null input and an english word
        """
        self.assertEqual(english_to_french(""), "Bonjour")
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    def test_assert_not_equal(self):
        """
        Method checks for inequality for null input and an english word
        """
        self.assertNotEqual(english_to_french(""), "Bonjour")
        self.assertNotEqual(english_to_french("Hello"), "Bonjour")
class TestFrenchToEnglish(unittest.TestCase):
    """
    Unit test class to check assertEqual for method english_to_french
    """
    def test_assert_equal(self):
        """
        Method checks for equality for null input and a french word
        """
        self.assertEqual(french_to_english(""), "Hello")
        self.assertEqual(french_to_english("Bonjour"), "Hello")
    def test_assert_not_equal(self):
        """
        Method checks for inequality for null input and a french word
        """
        self.assertNotEqual(french_to_english(""), "Hello")
        self.assertNotEqual(french_to_english("Bonjour"), "Hello")
unittest.main()
