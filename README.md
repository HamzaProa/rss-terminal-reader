# RSS Terminal Reader

A simple terminal-based RSS feed reader built in Python using [feedparser](https://pypi.org/project/feedparser/) and [rich](https://pypi.org/project/rich/).

## Features
- Parse multiple RSS feeds from `feeds.txt`
- Show feed items in a clean, colorful table
- Choose how many items to display with `--limit`
- Fetch all feeds at once with `--all`
- Open articles directly in your browser with `--open`

## Installation
Clone the repo and install dependencies:
```bash
git clone https://github.com/HamzaProa/rss-terminal-reader.git
cd rss-terminal-reader

# create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\activate

# install requirements
pip install -r requirements.txt
