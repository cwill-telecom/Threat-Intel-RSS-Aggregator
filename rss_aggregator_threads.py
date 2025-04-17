import feedparser
import csv
import threading
from datetime import datetime

# Curated RSS feeds from threat intel sources
rss_feeds = [
    "https://nao-sec.org/feed",
    "https://medium.com/feed/@sebdraven",
    "http://www.darknet.org.uk/feed/",
    "https://www.reddit.com/r/cybersecurity/.rss",
    "http://www.reddit.com/r/netsec/.rss",
    "https://www.bsi.bund.de/SiteGlobals/Functions/RSSFeed/RSSNewsfeed/RSSNewsfeed.xml",
    "https://www.cisecurity.org/feed/advisories",
    "https://resources.infosecinstitute.com/topics/malware-analysis/feed/",
    "https://resources.infosecinstitute.com/topics/news/feed/",
    "https://resources.infosecinstitute.com/topics/threat-intelligence/feed/",
    "https://www.nist.gov/blogs/cybersecurity-insights/rss.xml",
    "https://isc.sans.edu/rssfeed_full.xml",
    "https://us-cert.cisa.gov/ics/advisories/advisories.xml",
    "https://us-cert.cisa.gov/ncas/alerts.xml",
    "https://us-cert.cisa.gov/ncas/analysis-reports.xml",
    "https://us-cert.cisa.gov/ncas/current-activity.xml",
    "https://medium.com/feed/anton-on-security",
    "https://arstechnica.com/tag/security/feed/",
    "https://www.bellingcat.com/feed/",
    "https://www.bleepingcomputer.com/feed"
]

# Shared storage for collected articles
all_articles = []
lock = threading.Lock()

def fetch_rss(feed_url):
    try:
        feed = feedparser.parse(feed_url)
        items = [
            {
                "title": entry.title,
                "link": entry.link,
                "published": entry.get("published", "N/A"),
                "source": feed_url
            }
            for entry in feed.entries[:5]
        ]
        if not items:
            print(f"   ❌ No articles found from: {feed_url}")
        with lock:
            all_articles.extend(items)
        for article in items:
            print(f"   - ({article['published']}) {article['title']}")
    except Exception as e:
        print(f"   ❌ Error fetching {feed_url}: {e}")

def save_to_csv(data, filename="rss_articles.csv"):
    with open(filename, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "link", "published", "source"])
        writer.writeheader()
        for item in data:
            writer.writerow(item)

if __name__ == "__main__":
    threads = []

    for url in rss_feeds:
        print(f"\n[+] Fetching: {url}")
        thread = threading.Thread(target=fetch_rss, args=(url,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    if all_articles:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        csv_filename = f"rss_articles_{timestamp}.csv"
        save_to_csv(all_articles, csv_filename)
        print(f"\n✅ Saved {len(all_articles)} articles to: {csv_filename}")
    else:
        print("\n⚠️ No articles were collected.")
