from aqt import gui_hooks

# Anki imports
from aqt import mw
from aqt.qt import QAction, QDialog, QVBoxLayout
import sys
import os
import re


# Ensure src directory is in sys.path for Anki add-on loading
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

# PyQt6 import for webview (Anki Qt6)
try:
    from PyQt6.QtWebEngineWidgets import QWebEngineView
except ImportError:
    QWebEngineView = None

# Standard imports
import os
import json
from datetime import datetime



# Local module imports

from data_model import Card, Review, ProgressAggregator
from hsk_bar_chart import render_hsk_bar_charts


def render_chinese_progress_html():
    cards = get_cards_from_anki()
    aggregator = ProgressAggregator(cards)
    hsk_stats = aggregator.hsk_stats()
    # Render HSK bar chart HTML (D3.js)
    from hsk_bar_chart import render_hsk_bar_charts
    hsk_html = render_hsk_bar_charts(hsk_stats)
    # Render known words area chart HTML (D3.js)
    progress_data = aggregator.known_words_over_time()
    template_path = os.path.join(os.path.dirname(__file__), "known_words_area_chart_template.html")
    with open(template_path, "r", encoding="utf-8") as f:
        area_html = f.read()
    import json, re
    data_json = json.dumps(progress_data)
    area_html = re.sub(r"const progressData =[^;]*;", f"const progressData = {data_json};", area_html)
    # Compose both charts in the deck browser
    words_count = aggregator.total_known_words()
    chars_count = aggregator.total_known_characters()
    return f"""
    <div id='chinese-learn-progress' style='margin-top:24px;'>
        <h2>Chinese Progress</h2>
        <div style='font-size:1.1em; margin-bottom:12px;'>
            <b>Total Known Words:</b> {words_count} &nbsp; | &nbsp; <b>Total Known Characters:</b> {chars_count}
        </div>
        <div style='margin-bottom:32px;'>{hsk_html}</div>
        <div style='margin-bottom:32px;'>{area_html}</div>
    </div>
    """


def inject_chinese_progress(deck_browser, content):
    # For deck browser, append to content.stats
    if hasattr(content, "stats"):
        content.stats += render_chinese_progress_html()
        return content
    # Fallback for other contexts
    elif hasattr(content, "content"):
        content.content += render_chinese_progress_html()
        return content
    else:
        html = str(content)
        html += render_chinese_progress_html()
        return html

gui_hooks.deck_browser_will_render_content.append(inject_chinese_progress)

class KnownWordsAreaChartWebView(QWebEngineView):
    def __init__(self, parent=None):
        super().__init__(parent)
        cards = get_cards_from_anki()
        aggregator = ProgressAggregator(cards)
        progress_data = aggregator.known_words_over_time()
        template_path = os.path.join(os.path.dirname(__file__), "known_words_area_chart_template.html")
        with open(template_path, "r", encoding="utf-8") as f:
            html = f.read()
        data_json = json.dumps(progress_data)
        html = html.replace(
            "const progressData = [\n            { date: \"2025-10-01\", known_words: 50 },\n            { date: \"2025-10-02\", known_words: 52 },\n            { date: \"2025-10-03\", known_words: 55 },\n            { date: \"2025-10-04\", known_words: 60 },\n            { date: \"2025-10-05\", known_words: 65 }\n        ];",
            f"const progressData = {data_json};"
        )
        self.setHtml(html)

def show_known_words_area_chart():
    dialog = QDialog(mw)
    dialog.setWindowTitle("Known Words Over Time")
    layout = QVBoxLayout()
    webview = KnownWordsAreaChartWebView()
    layout.addWidget(webview)
    dialog.setLayout(layout)
    dialog.resize(1000, 500)
    dialog.exec()

def add_area_chart_menu_item():
    action = QAction("Known Words Over Time", mw)
    action.triggered.connect(show_known_words_area_chart)
    mw.form.menuTools.addAction(action)

add_area_chart_menu_item()
# Anki Learn Chinese Stats Extension
# Entry point for D3.js-based HSK bar chart in deck browser

def get_cards_from_anki():
    col = mw.col
    cards = []
    for cid in col.find_cards(''):  # get all cards
        card_obj = col.get_card(cid)
        note = card_obj.note()
        simplified = None
        if 'Simplified' in note.keys():
            simplified_idx = note.keys().index('Simplified')
            simplified = note.fields[simplified_idx]
        else:
            simplified = note.fields[0]
        tags = list(note.tags)
        interval = getattr(card_obj, 'ivl', 0)
        ease = getattr(card_obj, 'factor', 2500) / 1000.0
        # Get review history (dummy: only last review)
        reviews = []
        if interval > 0:
            last_review = datetime.fromtimestamp(card_obj.mod)
            # Dummy response: assume 'Good' if interval > 21, else 'Again'
            response = 'Good' if interval > 21 else 'Again'
            reviews.append(Review(last_review, response))
        cards.append(Card(cid, simplified, tags, reviews, interval, ease))
    return cards

class ChineseVocabWebView(QWebEngineView):
    def __init__(self, parent=None):
        super().__init__(parent)
        cards = get_cards_from_anki()
        aggregator = ProgressAggregator(cards)
        words_count = aggregator.total_known_words()
        chars_count = aggregator.total_known_characters()
        hsk_stats = aggregator.hsk_stats()
        hsk_data = []
        for level, stats in hsk_stats.items():
            hsk_data.append({"level": level, "total": stats["total"], "known": stats["known"]})
        # Write debug info to log file only
        debug_path = os.path.join(os.path.dirname(__file__), "chinese_learn_progress_debug.log")
        template_path = os.path.join(os.path.dirname(__file__), "hsk_bar_chart_template.html")
        with open(template_path, "r", encoding="utf-8") as f:
            html = f.read()
        data_json = json.dumps(hsk_data)
        # Robustly replace any line starting with 'const hskStats ='
        html = re.sub(r"const hskStats =[^;]*;", f"const hskStats = {data_json};", html)
        # Add fallback message if no chart is rendered
        with open(debug_path, "a", encoding="utf-8") as dbg:
            dbg.write("\n--- FINAL HTML ---\n")
            dbg.write(html)
            dbg.write("\n--- END FINAL HTML ---\n")
            dbg.write(f"words_count: {words_count}\n")
            dbg.write(f"chars_count: {chars_count}\n")
            dbg.write(f"hsk_data: {hsk_data}\n")
            dbg.write(f"template_path: {template_path}\n")
        self.setHtml(html)

def show_chinese_vocab_stats():
    dialog = QDialog(mw)
    dialog.setWindowTitle("Chinese Vocabulary Progress")
    layout = QVBoxLayout()
    webview = ChineseVocabWebView()
    layout.addWidget(webview)
    dialog.setLayout(layout)
    dialog.resize(1000, 500)
    dialog.exec()

def add_menu_item():
    action = QAction("Chinese Vocabulary Progress", mw)
    action.triggered.connect(show_chinese_vocab_stats)
    mw.form.menuTools.addAction(action)

add_menu_item()
# Anki Learn Chinese Stats Extension
# Basic add-on entry point
