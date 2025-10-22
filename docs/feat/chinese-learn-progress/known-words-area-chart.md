# Known Words Area Chart Design & Implementation

## Goal
Visualize progress of "known" words over time:
- X-axis: dates
- Y-axis: cumulative count of "known" words
- Smooth area fill to show growth
- Highlight milestones and trends

## Data Requirements
- For each date:
  - Cumulative number of unique "known" words
- Source: Card review history and "known" status changes

## Chart Design
- Area chart (line with filled area below)
- X-axis: chronological dates (daily granularity)
- Y-axis: cumulative "known" words
- Tooltip: shows date and count
- Milestone markers (optional)
- Responsive and theme-compatible

## Example Data Structure
```python
progress_over_time = [
    {'date': '2025-10-01', 'known_words': 50},
    {'date': '2025-10-02', 'known_words': 52},
    # ...
]
```

## Implementation Steps
1. Aggregate cumulative "known" words by date from review history
2. Choose charting library (e.g., Chart.js, Plotly, or Anki's built-in HTML/CSS)
3. Render area chart in deck browser view
4. Add tooltips and milestone markers
5. Test responsiveness and accessibility

## Best Practices
- Efficient data aggregation for large decks
- Modular chart rendering code
- Separate data/model from UI logic
- Use accessible color palette
- Document chart integration and customization

---
Design and code samples will be updated here as implementation progresses.
