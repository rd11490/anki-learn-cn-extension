# HSK Level Bar Chart Renderer
"""
Renders bar charts for each HSK level using HTML and CSS for Anki deck browser integration.
"""
from typing import Dict

HSK_COLORS = {
    "HSK1": "#4CAF50",
    "HSK2": "#2196F3",
    "HSK3": "#FFC107",
    "HSK4": "#FF5722",
    "HSK5": "#9C27B0",
    "HSK6": "#607D8B",
}

def render_hsk_bar_charts(hsk_stats: Dict[str, Dict[str, int]]) -> str:
    html = '<div class="hsk-bar-charts">'
    for level, stats in hsk_stats.items():
        total = stats["total"]
        known = stats["known"]
        percent = (known / total * 100) if total else 0
        color = HSK_COLORS.get(level, "#888")
        html += f'''
        <div class="hsk-bar-row">
            <span class="hsk-label">{level}</span>
            <div class="hsk-bar-outline" style="background:#eee; border:1px solid {color}; width:200px; height:24px; position:relative;">
                <div class="hsk-bar-fill" style="background:{color}; width:{percent}%; height:100%;"></div>
                <span class="hsk-bar-text" style="position:absolute; left:50%; top:0; transform:translateX(-50%); color:#222; font-size:14px;">{known}/{total}</span>
            </div>
        </div>
        '''
    html += '</div>'
    return html
