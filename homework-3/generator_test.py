from unittest import TestCase
from generator import generate_phrase


class TestGeneratePhrase(TestCase):

    # Function returns true for characters that can generate a word/phrase
    def test_valid_generator(self):
        test = generate_phrase("gfedcba", "abcdefg")
        self.assertTrue(test)

    # Function returns false for characters that cannot generate a word/phrase
    def test_invalid_generator(self):
        test = generate_phrase("anunkkaa", "nanaakua")
        self.assertFalse(test)

    # Function returns true for special characters, numbers and spaces
    def test_true_for_special_characters(self):
        test = generate_phrase("3!ne% Gatrr0", "Gen 3rat0r%!")
        self.assertTrue(test)

    # Function returns false for unequal (too short) characters word/phrase
    def test_false_for_short_characters(self):
        test = generate_phrase("cbacba", "aaabbbccc")
        self.assertFalse(test)
