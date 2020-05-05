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

LINK = 'https://www.milanofinanza.it/news/mercati/la-giornata-su-etfplus/'
source = 'milanofinanza_etf_'

# LINK = 'https://www.milanofinanza.it/news/mercati/la-giornata-sul-mot-euro-obbligazioni'
# source = 'milanofinanza_'

# LINK = 'https://www.milanofinanza.it/news/ingestione/gestioni-e-consulenti'
# source = 'milanofinanza_consulenti_'

result_map = pd.DataFrame()

# TO-MODIFY
# inserischi il numero + 1 di pagine presenti nell'archivio del Sole24ore (es: 8 schede -> n_pages = 9)
start_page = 90
finish_page = 99

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
            date = news[i].find("time").text
            driver.get('https://www.milanofinanza.it' + str(news_link))
            print(title, date)
            driver_checked = wait.until(presence_of_element_located((By.CLASS_NAME, "corpo-articolo")))
            pagenews_html = driver_checked.get_attribute('innerHTML')
            soap_news = BeautifulSoup(pagenews_html, 'html.parser')
            content = soap_news.find("p").text
            print(content)

            # creazione del df
            row_dict = { 'news_link': news_link, 'title': title, 'content': content, 'date': date }
            result_map = result_map.append([row_dict])
        
result_map.to_csv(source + str(start_page) + 'to'+ str(finish_page) + '.csv')

