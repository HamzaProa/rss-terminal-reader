import feedparser
from rich.console import Console

console = Console()

def read_rss(url):
    feed = feedparser.parse(url)
    title = getattr(feed.feed, "title", url)
    console.print(f"\n[bold green]{title}[/bold green]\n")
    for entry in feed.entries[:5]:
        console.print(f"- [bold cyan]{entry.title}[/bold cyan]")
        console.print(f"  {entry.link}\n")

if __name__ == "__main__":
    url = input("Enter RSS feed URL: ")
    read_rss(url)
