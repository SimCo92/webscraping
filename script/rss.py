import feedparser
import urllib.request
from bs4 import BeautifulSoup

NewsFeed = feedparser.parse("https://www.ilsole24ore.com/rss/finanza.xml")
entry = NewsFeed.entries[1]

# dict_keys(['title',
#  'title_detail',
#  'summary',
#  'summary_detail',
#  'links',
#  'link',
#  'authors',
#  'author',
#  'author_detail',
#  'id',
#  'guidislink',
#  'tags',
#  'published',
#  'published_parsed'])


for n,entry in enumerate(NewsFeed.entries):
    print('----------------------- NEWS',n,'--------------------------\n')
    print('title:',entry.title,'\n')
    print('summary:',entry.summary,'\n')
    print('link:',entry.link,'\n')
    print('published:',entry.published,'\n')
    
    request = urllib.request.Request(entry.link)
    html = urllib.request.urlopen(request).read()
    soup = BeautifulSoup(html,'html.parser')
    main_table = soup.findAll("p",attrs={'class':'atext'})
    
    print(main_table,'\n')