# c:\>c:\Python35\python -m venv c:\path\to\myenv

# cmd.exe
# C:\> <venv>\Scripts\activate.bat

# PowerShell
# PS C:\> <venv>\Scripts\Activate.ps1


import requests
import urllib.request
import datetime
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time

date = str(datetime.date.today())

# LINK = 'https://www.milanofinanza.it/news/mercati/la-giornata-su-etfplus/'
# source = 'etf'
# LINK = 'https://www.milanofinanza.it/news/mercati/la-giornata-sul-mot-euro-obbligazioni/'
# source = 'obligazioni'
# LINK = 'https://www.milanofinanza.it/news/ingestione/gestioni-e-consulenti/'
# source = 'consulenti'
# LINK = 'https://www.milanofinanza.it/news/lifestyle/salute/'
# source = 'salute' # 31
# LINK = 'https://www.milanofinanza.it/news/automotive/motori-su-strada/'
# source = 'motori-su-strada'
# LINK = 'https://www.milanofinanza.it/news/automotive/innovazione-e-tecnologia/'
# source = 'innovazione-e-tecnologia'
# LINK = 'https://www.milanofinanza.it/news/mondo/italia/'
# source = 'italia' # fino 50
# LINK = 'https://www.milanofinanza.it/news/business/energia/'
# source = 'energia'
# LINK = 'https://www.milanofinanza.it/news/business/media-tlc/'
# source = 'media-tlc'
# LINK = 'https://www.milanofinanza.it/news/business/industria/'
# source = 'industria' # sono 3000 pagine fatto fino 50
# LINK = 'https://www.milanofinanza.it/news/business/immobiliare/'
# source = 'immobiliare'
# LINK = 'https://www.milanofinanza.it/news/business/banche/'
# source = 'banche' # sono 1700 pagine fino a 50
# LINK = 'https://www.milanofinanza.it/news/business/assicurazioni/'
# source = 'assicurazioni'
# LINK = 'https://www.milanofinanza.it/news/business/utility/'
# source = 'utility' # sono 266 fatto fino 50
# LINK = 'https://www.milanofinanza.it/news/business/reatail-gdo/'
# source = 'retail-gdo'

result_map = pd.DataFrame()

# TO-MODIFY
# inserischi il numero + 1 di pagine presenti nell'archivio del Sole24ore (es: 8 schede -> n_pages = 9)
start_page = 1
finish_page = 50

path = os.getcwd() + '/chromedriver'
with webdriver.Chrome(path) as driver:
    wait = WebDriverWait(driver, 10)
    for n in range(start_page,finish_page):
        LINKn = LINK + str(n)
        response = requests.get(LINKn)
        print('processing: ', LINKn)
        driver.get(LINKn)
        driver_checked = wait.until(presence_of_element_located((By.CLASS_NAME, "primo-piano")))
        page_html = driver_checked.get_attribute('innerHTML')
        while len(page_html) < 500:
            print('LOADING ERROR')
            time.sleep(3)
            driver_checked = wait.until(presence_of_element_located((By.CLASS_NAME, "primo-piano")))
            page_html = driver_checked.get_attribute('innerHTML')
        soap = BeautifulSoup(page_html, 'html.parser')
        news = soap.findAll("li")
        

        # loop all'interno di tutti gli articoli presenti nella stessa pagina
        resultxpage = len(news)
        for i in range(resultxpage):
            news_link = news[i].find("h3").find("a")['href']
            title = news[i].find("h3").find("a").text
            short_content = news[i].find("p").text
            date = news[i].find("time").text
            driver.get('https://www.milanofinanza.it' + str(news_link))
            print(news_link, title, short_content)
            driver_checked = wait.until(presence_of_element_located((By.CLASS_NAME, "corpo-articolo")))
            pagenews_html = driver_checked.get_attribute('innerHTML')
            soap_news = BeautifulSoup(pagenews_html, 'html.parser')
            content_complete = soap_news.text
            try:
                content_list = soap_news.findAll("p")
                n_chapters = len(content_list)
                content = ''
                for i in range(n_chapters):
                    content = content + str(content_list[i].text)
            except:
                content = None

            # creazione del df
            row_dict = { 'news_link': news_link, 'title': title, 'short_content': short_content, 'content_complete' : content_complete, 'content': content, 'date': date }
            result_map = result_map.append([row_dict])
        
result_map.to_csv('milanofinanza_' + source + '.csv')

