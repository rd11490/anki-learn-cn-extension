# chinese-learn-progress Feature Implementation Plan

## Goal
Display a graphical summary in the Anki deck browser showing:
- Total Number of Chinese Words Learned
- Total Number of Chinese Characters Learned
- Bar Charts for each HSK Level:
  - Bar outline: total cards tagged with HSK level
  - Bar fill: cards considered "known"
- Area Chart: x-axis = dates, y-axis = words considered "known" (progress over time)

## Data Sources
- Anki card collection
- Card tags (HSK level)
- Card fields (Chinese words/characters)
- Card review history (for progress over time)

## Components
1. **Data Model**
   - Parse cards for Chinese words/characters
   - Track HSK level via tags
   - Determine "known" status (e.g., mature, review count, ease)
   - Aggregate review history for time series

2. **Bar Charts (HSK Levels)**
   - For each HSK level:
     - Outline: total cards tagged
     - Fill: cards considered "known"
   - Interactive tooltips for details

3. **Area Chart (Progress Over Time)**
   - X-axis: date
   - Y-axis: cumulative "known" words
   - Smooth area fill, highlight milestones

4. **Deck Browser Integration**
   - Inject charts into deck browser UI
   - Responsive layout, theme compatibility
   - Best practices for Anki add-on structure

5. **Styling & Design**
   - Modern, clean chart styles
   - Color palette for HSK levels
   - Accessibility and readability

## Implementation Steps
1. Define data extraction and aggregation logic
2. Build chart rendering components (bar, area)
3. Integrate with deck browser view
4. Test with sample data and real decks
5. Refine design and UX
6. Document code and design decisions

## Best Practices
- Modular code structure
- Separation of data/model and UI/view
- Use established charting libraries if possible
- Follow Anki add-on guidelines
- Document all design choices and progress

---
Progress and design decisions will be tracked in `docs/feat/chinese-learn-progress/`.
