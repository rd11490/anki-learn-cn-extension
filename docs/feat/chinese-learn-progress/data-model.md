# Data Model Design: Learned Words & Characters

## Overview
This document outlines the data model and logic for calculating:
- Total Chinese words learned
- Total Chinese characters learned
- "Known" status for each card
- HSK level aggregation
- Progress over time

## Card Data Extraction
- **Source:** Anki card collection
- **Fields Used:**
  - `simplified`: Contains the Chinese word/phrase (may be multiple characters)
  - `tags`: Used to determine HSK level (e.g., `HSK1`, `HSK2`, ...)
  - Review history: Used for maturity and "known" status

## Data Structures

### Card Object
```python
class Card:
    id: int
    simplified: str  # Chinese word/phrase
    characters: List[str]  # Individual characters
    tags: List[str]  # HSK level tags
    reviews: List[Review]  # Review history
    interval: int  # Days until next review
    ease: float  # Ease factor
    is_known: bool  # Calculated "known" status
```

### Review Object
```python
class Review:
    date: datetime
    response: str  # e.g., "Again", "Hard", "Good", "Easy"
```

## Logic for "Known" Status
- Card is "known" if:
  - `interval > 21` days
  - `ease > 2.5`
  - Last review response was not "Again" or "Hard"
- Card loses "known" status if last review response is "Again" or "Hard"

## Aggregation
- **Total Words Learned:** Count of unique `simplified` values for cards with `is_known = True`
- **Total Characters Learned:** Count of unique characters from all `simplified` fields of cards with `is_known = True`
- **HSK Level Aggregation:**
  - For each HSK level:
    - Total cards tagged
    - Total "known" cards
- **Progress Over Time:**
  - For each date, count cumulative "known" words

## Example Workflow
1. Parse all cards in collection
2. For each card:
   - Extract `simplified`, split into characters
   - Check tags for HSK level
   - Analyze review history for maturity and last response
   - Set `is_known` status
3. Aggregate totals and chart data

## Next Steps
- Implement Card and Review classes
- Write logic for extracting and aggregating data
- Prepare data for chart rendering

---
Design decisions and code samples will be updated here as implementation progresses.
