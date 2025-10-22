import unittest
from datetime import datetime
from chinese_learn_progress.data_model import Card, Review, ProgressAggregator

class TestDataModel(unittest.TestCase):
    def setUp(self):
        # Create sample reviews
        self.reviews1 = [
            Review(datetime(2025, 10, 1), "Good"),
            Review(datetime(2025, 10, 10), "Easy"),
        ]
        self.reviews2 = [
            Review(datetime(2025, 10, 2), "Hard"),
            Review(datetime(2025, 10, 12), "Good"),
        ]
        self.reviews3 = [
            Review(datetime(2025, 10, 3), "Again"),
            Review(datetime(2025, 10, 13), "Good"),
        ]
        # Create sample cards
        self.card1 = Card(1, "你好", ["HSK1"], self.reviews1, interval=30, ease=2.6)
        self.card2 = Card(2, "谢谢", ["HSK1", "HSK2"], self.reviews2, interval=22, ease=2.7)
        self.card3 = Card(3, "再见", ["HSK2"], self.reviews3, interval=10, ease=2.4)
        self.cards = [self.card1, self.card2, self.card3]
        self.aggregator = ProgressAggregator(self.cards)

    def test_known_status(self):
        self.assertTrue(self.card1.is_known)
        self.assertTrue(self.card2.is_known)
        self.assertFalse(self.card3.is_known)

    def test_total_known_words(self):
        self.assertEqual(self.aggregator.total_known_words(), 2)

    def test_total_known_characters(self):
        # "你好" and "谢谢" = 3 unique characters
        self.assertEqual(self.aggregator.total_known_characters(), 3)

    def test_hsk_stats(self):
        stats = self.aggregator.hsk_stats()
        self.assertEqual(stats["HSK1"], {"total": 2, "known": 2})
        self.assertEqual(stats["HSK2"], {"total": 2, "known": 1})

    def test_known_words_over_time(self):
        progress = self.aggregator.known_words_over_time()
        self.assertTrue(any(p["known_words"] == 1 for p in progress))
        self.assertTrue(any(p["known_words"] == 2 for p in progress))

if __name__ == "__main__":
    unittest.main()
