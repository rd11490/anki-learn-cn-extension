# HSK Level Bar Chart Renderer
"""
Renders bar charts for each HSK level using HTML and CSS for Anki deck browser integration.
"""
from typing import Dict
import json
import os
import re

HSK_COLORS = {
    "HSK1": "#4CAF50",
    "HSK2": "#2196F3",
    "HSK3": "#FFC107",
    "HSK4": "#FF5722",
    "HSK5": "#9C27B0",
    "HSK6": "#607D8B",
}

def render_hsk_bar_charts(hsk_stats: Dict[str, Dict[str, int]]) -> str:
    # Load the D3.js template
    template_path = os.path.join(os.path.dirname(__file__), "hsk_bar_chart_template.html")
    with open(template_path, "r", encoding="utf-8") as f:
        html = f.read()
    data = []
    for level, stats in hsk_stats.items():
        data.append({"level": level, "total": stats["total"], "known": stats["known"]})
    data_json = json.dumps(data)
    html = re.sub(r"const hskStats =[^;]*;", f"const hskStats = {data_json};", html)
    return html
