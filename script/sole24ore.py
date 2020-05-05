import requests
import urllib.request
import datetime
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

date = str(datetime.date.today())

# LINK = 'https://www.ilsole24ore.com/archivi/finanza/quotate-italia/'
LINK = 'https://www.ilsole24ore.com/archivi/finanza/quotate-mondo/'
result_map = pd.DataFrame()

# TO-MODIFY
# inserischi il numero + 1 di pagine presenti nell'archivio del Sole24ore (es: 8 schede -> n_pages = 9)
n_pages = 6

for n in range(1,n_pages):
    LINKn = LINK + str(n)
    response = requests.get(LINKn)
    print('processing: ', LINKn)
    soup = BeautifulSoup(response.text, 'html.parser')
    raw = soup.findAll("li", {"class": "list-lined-item"})

    # loop all'interno di tutti gli articoli presenti nella stessa pagina
    resultxpage = len(raw)
    for i in range(resultxpage):
        text = raw[i].text
        meta = raw[i].findAll("a", {"class": "meta-part"})
        title = raw[i].findAll("h3", {"class": "aprev-title"})[0].text
        topic = meta[0].text

        # scraping all'interno dell'articolo - questa parte del codice puo essere scorporata in una nuova funzione
        news_link = 'https://www.ilsole24ore.com' + meta[0]['href']
        response_news = requests.get(news_link)
        soup_news = BeautifulSoup(response_news.text, 'html.parser')
        date_news = soup_news.find("time", {"class": "time"}).text
        raw_news = soup_news.find("div", {"class": "aentry--lined"})
        news_soup = raw_news.findAll("p", {"class": "atext"})
        if not news_soup:
            print('ERROR in the article: ', news_link )
        n_chapters = len(news_soup)
        news_content = ''
        for i in range(n_chapters):
            news_content = news_content + str(news_soup[i].text)

        # creazione del df
        row_dict = { 'news_link': news_link, 'topic': topic, 'title': title, 'content': news_content, 'date': date_news}
        result_map = result_map.append([row_dict])
        
result_map.to_csv('sole24ore_mondo_' + date + '.csv')

