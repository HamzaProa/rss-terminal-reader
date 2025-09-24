import argparse
import webbrowser
from pathlib import Path

import feedparser
from rich.console import Console
from rich.table import Table
from rich.prompt import IntPrompt, Prompt

console = Console()

def load_feeds(path: Path) -> list[str]:
    if not path.exists():
        console.print(f"[yellow]No feeds file found at {path}. Create one with one URL per line.[/yellow]")
        return []
    feeds = [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip() and not line.startswith("#")]
    if not feeds:
        console.print(f"[yellow]{path} is empty. Add some feed URLs.[/yellow]")
    return feeds

def fetch_feed(url: str):
    feed = feedparser.parse(url)
    title = getattr(feed.feed, "title", url)
    return title, feed.entries

def print_entries(title: str, entries, limit: int):
    table = Table(title=title)
    table.add_column("#", justify="right", no_wrap=True)
    table.add_column("Title")
    table.add_column("Link")
    for i, e in enumerate(entries[:limit], start=1):
        table.add_row(str(i), e.get("title", "(no title)"), e.get("link", ""))
    console.print(table)

def choose(options: list[str], prompt: str) -> int:
    """Return zero-based index of selected option."""
    for i, opt in enumerate(options, start=1):
        console.print(f"[cyan]{i}[/cyan]. {opt}")
    idx = IntPrompt.ask(prompt, choices=[str(i) for i in range(1, len(options)+1)])
    return int(idx) - 1

def main():
    parser = argparse.ArgumentParser(description="Terminal RSS reader")
    parser.add_argument("--feeds", default="feeds.txt", help="Path to feeds list (one URL per line)")
    parser.add_argument("--limit", type=int, default=5, help="Max articles to show")
    parser.add_argument("--all", action="store_true", help="Fetch all feeds instead of choosing one")
    parser.add_argument("--open", action="store_true", help="After listing, choose an item to open in browser")
    args = parser.parse_args()

    feeds = load_feeds(Path(args.feeds))
    if not feeds:
        url = Prompt.ask("Enter an RSS feed URL")
        feeds = [url]

    if args.all and len(feeds) > 1:
        for url in feeds:
            title, entries = fetch_feed(url_
