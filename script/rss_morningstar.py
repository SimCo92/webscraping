import feedparser

python_wiki_rss_url = "https://www.morningstar.it/it/news/rss.aspx?lang=it-IT"
feed = feedparser.parse( python_wiki_rss_url )

print(feed)