import requests
import urllib.request
import datetime
from bs4 import BeautifulSoup

date = str(datetime.date.today())

LINK = 'https://www.ilsole24ore.com/archivi/finanza/quotate-italia/'

# for n in range(1,13):
for n in range(1,3):
    LINKn = LINK + str(n)
    response = requests.get(LINKn)
    print(LINKn)
    soup = BeautifulSoup(response.text, 'html.parser')
    raw = soup.findAll("li", {"class": "list-lined-item"})
    resultxpage = len(raw)
    for i in range(resultxpage):
        text = raw[i].text
        meta = raw[i].findAll("a", {"class": "meta-part"})
        title = raw[i].findAll("h3", {"class": "aprev-title"})[0].text
        href = meta[0]['href']
        link = 'www.ilsole24ore.com' + href
        topic = meta[0].text
        print(title)
        print(link)
        print(topic)