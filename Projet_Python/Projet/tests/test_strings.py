import unittest
from words.strings import count_words, count_chars, check_string


class StringsTestCase(unittest.TestCase):

    def test_check_string(self):
        with self.assertRaises(Exception):
            check_string(None)
        self.assertIsNone(check_string(""))
        self.assertIsNone(check_string("Hello"))

    def test_count_words(self):
        self.assertEqual(count_words("Hello There!"), 2)
        self.assertEqual(count_words("Hello There !"), 3)
        self.assertEqual(count_words(""), 0)
        with self.assertRaises(Exception):
            count_words(None)

    def test_count_chars(self):
        self.assertEqual(count_chars("Hello There!"), 12)
        self.assertEqual(count_chars("Hello There !"), 13)
        self.assertEqual(count_chars(""), 0)
        with self.assertRaises(Exception):
            count_chars(None)
