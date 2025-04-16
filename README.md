# 🛰️ Threat Intel RSS Aggregator

This Python script aggregates the latest articles from curated RSS feeds across cybersecurity, threat intelligence, malware analysis, and vulnerability advisories. It parses feeds from leading security blogs, research communities, and government organizations, saving the top entries to a timestamped CSV file.

## 📌 Features

- Pulls content from 20+ threat intelligence RSS feeds
- Displays top 5 articles per source with titles and publish dates
- Outputs results into a clean, sortable CSV file
- Supports real-time progress and error handling for broken feeds

## 🧠 Use Cases

- Building a personal threat intel feed
- OSINT research aggregation
- Daily cybersecurity news summary
- Preprocessing input for ML/NLP pipeline

---

## 🛠️ Requirements

- Python 3.6+
- [feedparser](https://pypi.org/project/feedparser/)

Install the required dependency:

```bash
pip install feedparser
```

---

## 🚀 Usage

Run the script with:

```bash
python rss_aggregator.py
```

The script will:

1. Fetch the top 5 articles from each RSS feed
2. Display them in the terminal
3. Save the results to a file named like:

```
rss_articles_20250416_1415.csv
```

_(Date and time are automatically appended)_

---

## 📂 Output Format

The CSV includes:

| Title | Link | Published Date | Source Feed |
|-------|------|----------------|-------------|

Example:

```csv
title,link,published,source
"New Malware Campaign Targets IoT Devices","https://example.com/malware","Tue, 16 Apr 2025 13:45:00 GMT","https://resources.infosecinstitute.com/topics/malware-analysis/feed/"
...
```

---

## 🧩 Customization

You can modify the `rss_feeds` list to include your preferred sources:

```python
rss_feeds = [
    "https://example.com/feed",
    ...
]
```

Adjust the number of articles retrieved per feed by editing the `[:5]` slice in `fetch_rss()`.

---

## ⚠️ Known Limitations

- Feed content varies in structure and may occasionally cause parsing errors
- Heavy rate-limiting on some feeds may block frequent use
- No GUI interface (yet)

---

## 📖 License

This project is released under the MIT License.

---

## 🤝 Contributions

Pull requests and feed suggestions are welcome! Please open an issue or submit a PR to add new sources or functionality.

---

## 🧠 Credits

This script leverages open-source libraries and public feeds from:

- SANS ISC
- CISA
- Infosec Institute
- Reddit /r/netsec and /r/cybersecurity
- Bellingcat
- BleepingComputer
- Medium security researchers
- And others...
