# Deck Browser Integration Plan

## Goal
Integrate all graphical elements (HSK bar charts, known words area chart, totals) into the Anki deck browser view, following best practices for structure, design, and styling.

## Integration Points
- Inject custom HTML/CSS/JS into deck browser template
- Display charts and totals in a dedicated section (e.g., sidebar or top panel)
- Ensure compatibility with Anki themes and layouts

## Implementation Steps
1. Identify deck browser template hooks for add-on injection
2. Prepare chart rendering code (prefer modular JS, e.g., Chart.js)
3. Aggregate and format data for charts and totals
4. Inject HTML/CSS/JS for charts and summary display
5. Test integration with various decks and themes
6. Refine layout, responsiveness, and accessibility

## Best Practices
- Keep UI code modular and maintainable
- Separate data/model logic from view rendering
- Use scoped CSS to avoid conflicts
- Document integration points and customizations
- Provide fallback for non-JS environments

## Example Layout
```
+---------------------------------------------+
| Deck Browser                               |
|---------------------------------------------|
| [Chinese Progress Summary]                  |
|  - Total Words Learned                      |
|  - Total Characters Learned                 |
|  - HSK Level Bar Charts                     |
|  - Known Words Area Chart                   |
+---------------------------------------------+
```

---
Design and code samples will be updated here as implementation progresses.
