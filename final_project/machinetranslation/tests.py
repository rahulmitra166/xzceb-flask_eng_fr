import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """
    Unit test class for method english_to_french
    """
    def test_assert_equal_1(self):
        """
        Testing for equality
        """
        with self.subTest(msg='Check for en-fr assertEqual'):
            self.assertEqual(english_to_french("Hello"), "Bonjour")
    def test_assert_not_equal_1(self):
        """
        Testing for inequality
        """
        with self.subTest(msg='Check for en-fr assertNotEqual'):
            self.assertNotEqual(english_to_french("Hello"), "Bonjour")
class TestFrenchToEnglish(unittest.TestCase):
    """
    Unit test class for method english_to_french
    """
    def test_assert_equal_2(self):
        """
        Testing for equality
        """
        with self.subTest(msg='Check for fr-en assertEqual'):
            self.assertEqual(french_to_english("Bonjour"), "Hello")
    def test_assert_not_equal_2(self):
        """
        Testing for inequality
        """
        with self.subTest(msg='Check for fr-en assertNotEqual'):
            self.assertNotEqual(french_to_english("Bonjour"), "Hello")
unittest.main()
