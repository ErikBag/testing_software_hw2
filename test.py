import unittest
from main import search_text


class TestAhoCorasick(unittest.TestCase):

    def setUp(self):
        # Подготовка данных для тестов
        self.keywords = ["he", "she", "his", "hers", "she sells", "he is"]

    def test_search_basic(self):
        text = "ushers"
        result = search_text(text, self.keywords)
        expected = {
            "he": [2],
            "she": [1],
            "his": [],
            "hers": [2],
            "she sells": [],
            "he is": []
        }
        self.assertEqual(result, expected)

    def test_search_no_matches(self):
        text = "abcde"
        result = search_text(text, self.keywords)
        expected = {
            "he": [],
            "she": [],
            "his": [],
            "hers": [],
            "she sells": [],
            "he is": []
        }
        self.assertEqual(result, expected)

    def test_search_multiple_matches(self):
        text = "ahishers"
        result = search_text(text, self.keywords)
        expected = {
            "he": [4],
            "she": [3],
            "his": [1],
            "hers": [4],
            "she sells": [],
            "he is": []
        }
        self.assertEqual(result, expected)

    def test_search_empty_text(self):
        text = ""
        result = search_text(text, self.keywords)
        expected = {
            "he": [],
            "she": [],
            "his": [],
            "hers": [],
            "she sells": [],
            "he is": []
        }
        self.assertEqual(result, expected)

    def test_search_patterns_in_text(self):
        text = "she sells sea shells by the sea shore"
        result = search_text(text, self.keywords)
        expected = {
            "he": [1, 15, 25],
            "she": [0, 14],
            "his": [],
            "hers": [],
            "she sells": [0],
            "he is": []
        }
        self.assertEqual(result, expected)

    def test_search_overlapping_patterns(self):
        keywords = ["ab", "bc", "abc"]
        text = "abcabc"
        result = search_text(text, keywords)
        expected = {
            "ab": [0, 3],
            "bc": [1, 4],
            "abc": [0, 3]
        }
        self.assertEqual(result, expected)

    def test_search_with_special_characters(self):
        keywords = ["he", "she", "his", "hers", "hello"]
        text = "hello! she said he is his."
        result = search_text(text, keywords)
        expected = {
            "he": [0, 8, 16],
            "she": [7],
            "his": [22],
            "hers": [],
            "hello": [0]
        }
        self.assertEqual(result, expected)

    def test_search_duplicate_patterns(self):
        keywords = ["he", "he", "she"]
        text = "ushers"
        result = search_text(text, keywords)
        expected = {
            "he": [2, 2],
            "she": [1],
        }
        self.assertEqual(result, expected)

    def test_empty_text(self):
        keywords = ["he", "he", "she"]
        text = ""
        result = search_text(text, keywords)
        expected = {
            "he": [],
            "she": [],
        }
        self.assertEqual(result, expected)

    def test_empty_keywords(self):
        keywords = []
        text = "ushers"
        result = search_text(text, keywords)
        expected = {
        }
        self.assertEqual(result, expected)

    def test_empty_text_and_empty_keywords(self):
        keywords = []
        text = ""
        result = search_text(text, keywords)
        expected = {
        }
        self.assertEqual(result, expected)
