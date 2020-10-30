from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.remote.webdriver.WebDriver
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, presence_of_element_located

import requests
import datetime
import time
import os
from bs4 import BeautifulSoup
import pandas as pd
# import numpy as np

date = str(datetime.date.today())

path = os.getcwd() + '/chromedriver'
data = pd.read_csv("morningstar_map.csv")
content_df = pd.DataFrame()
content_dict = {}

with webdriver.Chrome(path) as driver:
    wait = WebDriverWait(driver, 5)

    for i,link_news in enumerate(data['link']):
        try:
            print('processing : ', link_news)
            driver.get(link_news)
            driver_news = wait.until(presence_of_element_located((By.CLASS_NAME, "mainContent")))
            pagenews_html = driver_news.get_attribute('innerHTML')
            soap_news = BeautifulSoup(pagenews_html, 'html.parser')

            # response = requests.get(link_news)
            # soup = BeautifulSoup(response.text, 'html.parser')
            # raw = soup.find("div", {"class": "mainContent"})

            content = soap_news.findAll("p")
            content_concat = ''
            for n in range(len(content)):
                content_concat = content_concat + str(content[n].text)
            # print(content_concat)
            
            content_dict = { 'link': link_news, 'content' : content_concat }
            content_df = content_df.append([content_dict])
            # print(content_df)

        except:
            print('ERROR')
            pass

        print('articles processed : ', i)

content_df.to_csv('morningstar_content.csv')
