# HSK Level Bar Charts Design & Implementation

## Goal
Visualize progress for each HSK level:
- Bar outline: total cards tagged with HSK level
- Bar fill: cards considered "known"
- Interactive tooltips for details

## Data Requirements
- For each HSK level (HSK1-HSK6):
  - Total number of cards tagged
  - Number of cards with `is_known = True`

## Chart Design
- Horizontal or vertical bar chart per HSK level
- Bar outline: represents total cards
- Bar fill: represents known cards
- Color-coded by HSK level
- Tooltip: shows counts and percentage known
- Responsive and theme-compatible

## Example Data Structure
```python
hsk_stats = {
    'HSK1': {'total': 120, 'known': 80},
    'HSK2': {'total': 100, 'known': 60},
    # ...
}
```

## Implementation Steps
1. Aggregate HSK stats from card data
2. Choose charting library (e.g., Chart.js, Plotly, or Anki's built-in HTML/CSS)
3. Render bar charts in deck browser view
4. Add tooltips and color styling
5. Test responsiveness and accessibility

## Best Practices
- Modular chart rendering code
- Separate data aggregation from UI logic
- Use accessible color palette
- Document chart integration and customization

---
Design and code samples will be updated here as implementation progresses.
