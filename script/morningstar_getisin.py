from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, presence_of_element_located

# import requests
import datetime
import time
import os
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

date = str(datetime.date.today())
path = os.getcwd() + '/chromedriver'

data = pd.read_csv("isin_map.csv")
data = data[data['link'] != 'missing']

content_df = pd.DataFrame()
content_dict = {}

with webdriver.Chrome(path) as driver:
    wait = WebDriverWait(driver, 5)

    for index, row in data.iterrows():
        if row['link'] == 'missing':
            content_dict = { 'link': row['link'], 'content' : none }

        else:
            print('processing : ', row['isin'], row['link'])
            driver.get(str('https://www.morningstar.it' + row['link']))
            try:
                WebDriverWait(driver, 5).until(element_to_be_clickable((By.ID, "finaprofessional"))).click()
                WebDriverWait(driver, 1).until(element_to_be_clickable((By.ID, "_evidon-accept-button"))).click()
                print('logging in')
            except:
                print('no login needed')

            wait.until(presence_of_element_located((By.ID, "mainContentDiv")))

            try:
                tableoverview = wait.until(presence_of_element_located((By.CLASS_NAME, "overviewPortfolioMixTable")))
                print('table found')
                page_html = tableoverview.get_attribute('innerHTML')
                table_html = BeautifulSoup(page_html, 'html.parser')
            except:
                table_html = None
                print('no table')
            

            content_dict = { 'link': row['link'], 'content' : table_html }
            content_df = content_df.append([content_dict])
            # print(content_df)

        print('articles processed : ', index)

content_df.to_csv('isin_scraped.csv')