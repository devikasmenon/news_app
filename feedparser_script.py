import feedparser

# List of RSS feeds
rss_feeds = [
    "http://rss.cnn.com/rss/cnn_topstories.rss",
    "http://qz.com/feed",
    "http://feeds.foxnews.com/foxnews/politics",
    "http://feeds.reuters.com/reuters/businessNews",
    "http://feeds.feedburner.com/NewshourWorld",
    "https://feeds.bbci.co.uk/news/world/asia/india/rss.xml"
]

# Function to collect news articles
def collect_news_articles():
    articles = []
    for feed_url in rss_feeds:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            article = {
                "title": entry.get('title', ''),
                "content": entry.get('summary', entry.get('description', '')),
                "publication_date": entry.get('published', ''),
                "source_url": entry.get('link', '')
            }
            articles.append(article)
    return articles


# Example usage:
if __name__ == "__main__":
    news_articles = collect_news_articles()
    for article in news_articles:
        print(article)
