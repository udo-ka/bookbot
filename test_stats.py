from unittest import TestCase, main
from stats import get_num_words


class TestStats(TestCase):
    def test_get_num_words(self):
        text = "Title: Frankenstein; Or, The Modern Prometheus"
        self.assertEqual(get_num_words(text), 6)


if __name__ == "__main__":
    main()
