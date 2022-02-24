import unittest
from utils.Levenshtein import levenshtein


class LevenshteinTest(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(levenshtein([0, 1, 2], [0, 1, 2]), 0)

    def test_len(self):
        self.assertEqual(levenshtein([0, 1], [0, 1, 2]), 1)
        self.assertEqual(levenshtein([0, 1, 2], [0, 1]), 1)

    def test_diff(self):
        self.assertEqual(levenshtein([0, 1, 2], [0, 1, 3]), 1)
        self.assertEqual(levenshtein([0, 1, 2], [1, 1, 2]), 1)

    def test_diff_len(self):
        self.assertEqual(levenshtein([0, 1], [0, 2, 3]), 2)
