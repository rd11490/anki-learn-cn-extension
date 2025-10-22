# chinese_learn_progress/data_model.py
"""
Data model for Chinese Learn Progress add-on.
Handles extraction and aggregation of learned words, characters, HSK levels, and known status from Anki cards.
"""
from typing import List, Dict, Optional
from datetime import datetime

class Review:
    def __init__(self, date: datetime, response: str):
        self.date = date
        self.response = response

class Card:
    def __init__(self, card_id: int, simplified: str, tags: List[str], reviews: List[Review], interval: int, ease: float):
        self.id = card_id
        self.simplified = simplified
        self.characters = list(simplified)
        self.tags = tags
        self.reviews = reviews
        self.interval = interval
        self.ease = ease
        self.is_known = self.calculate_known_status()

    def calculate_known_status(self) -> bool:
        # TEMPORARY: Treat any card with at least one review as known
        return bool(len(self.reviews or []) > 0)
        # --- Original known status logic ---
        # if self.interval > 21 and self.ease > 2.5:
        #     if self.reviews and self.reviews[-1].response not in ["Again", "Hard"]:
        #         return True
        # return False

class ProgressAggregator:
    def __init__(self, cards: List[Card]):
        self.cards = cards

    def total_known_words(self) -> int:
        return len(set(card.simplified for card in self.cards if card.is_known))

    def total_known_characters(self) -> int:
        chars = set()
        for card in self.cards:
            if card.is_known:
                chars.update(card.characters)
        return len(chars)

    def hsk_stats(self) -> Dict[str, Dict[str, int]]:
        hsk_levels = [f"HSK{i}" for i in range(1, 7)]
        stats = {}
        for level in hsk_levels:
            total = sum(level in card.tags for card in self.cards)
            known = sum(level in card.tags and card.is_known for card in self.cards)
            stats[level] = {"total": total, "known": known}
        return stats

    def known_words_over_time(self) -> List[Dict[str, int]]:
        date_to_known = {}
        for card in self.cards:
            for review in card.reviews:
                date_str = review.date.strftime("%Y-%m-%d")
                if card.is_known:
                    date_to_known.setdefault(date_str, set()).add(card.simplified)
        # Build cumulative count
        sorted_dates = sorted(date_to_known.keys())
        cumulative = set()
        progress = []
        for date in sorted_dates:
            cumulative.update(date_to_known[date])
            progress.append({"date": date, "known_words": len(cumulative)})
        return progress
