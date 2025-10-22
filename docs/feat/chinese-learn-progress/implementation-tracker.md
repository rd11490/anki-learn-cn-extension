# Implementation Tracker: chinese-learn-progress

This tracker documents progress, design decisions, and implementation notes for the graphical deck browser feature.

## Progress Checklist
- [x] Feature plan drafted (`feature-plan.md`)
- [ ] Data model for learned words/characters
- [ ] HSK level bar charts
- [ ] Known words area chart
- [ ] Deck browser integration
- [ ] Design and styling review

## Design Decisions
- **Data Extraction:** Use the `simplified` field on each card for words and characters.
- **"Known" Status Logic:**
  - Card is "known" if it reaches maturity (interval > 21 days, ease > 2.5).
  - If reviewed and marked incorrect (e.g., "Again" or "Hard"), it loses "known" status.
  - If marked correct ("Good" or "Easy"), it remains "known".
- **HSK Level:** Determined by card tags.
- **Progress Over Time:** Use review history to track "known" words by date.

## Next Steps
1. Implement data model for learned words/characters and "known" logic
2. Build chart components for HSK levels and progress over time
3. Integrate charts into deck browser
4. Refine design and styling

---
All updates and decisions should be logged here for transparency and future reference.
