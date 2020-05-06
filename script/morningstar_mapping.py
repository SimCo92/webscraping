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


LINK = 'https://www.morningstar.it/it/collection/3003/3104/news-fondi.aspx'

path = os.getcwd() + '/chromedriver'
# driver = webdriver.Firefox()

result_map = pd.DataFrame()

with webdriver.Chrome(path) as driver:
    wait = WebDriverWait(driver, 10)
    driver.get(LINK)

    # loop over sheets
    for i in range(50):

        # login
        try:
            WebDriverWait(driver, 5).until(element_to_be_clickable((By.ID, "finaprofessional"))).click()
            WebDriverWait(driver, 1).until(element_to_be_clickable((By.ID, "_evidon-accept-button"))).click()
            print('logging in')
        except:
            print('no login needed')
        
        print('processing sheet n', i)
        driver_checked = wait.until(presence_of_element_located((By.CSS_SELECTOR, "tbody")))

        try:
            page_html = driver_checked.get_attribute('innerHTML')
        except:
            print('sleeping')
            time.sleep(10)
            page_html = driver_checked.get_attribute('innerHTML')

        soap = BeautifulSoup(page_html, 'html.parser')
        news = soap.findAll("tr")
        
        #  loop of sheet news
        for i in range(len(news)):
            title = news[i].find("td", {"headers": "archive_title"}).text
            link = news[i].find("td", {"headers": "archive_title"}).find("a")['href']
            date = news[i].find("td", {"headers": "archive_date"}).text
            
            # print(link)
            # try:
            #     driver.get(str(link))
            #     driver_news = wait.until(presence_of_element_located((By.CLASS_NAME, "mainContent")))
            #     pagenews_html = driver_news.get_attribute('innerHTML')
            #     soap_news = BeautifulSoup(pagenews_html, 'html.parser')

            #     content = soap_news.findAll("p")
            #     content_concat = ''
            #     for n in range(len(content)):
            #         content_concat = content_concat + str(content[n].text)
            
            #     print(title, content_concat)

            #     row_dict = { 'link': link, 'title': title, 'content': content_concat, 'date': date }
            #     result_map = result_map.append([row_dict])
            # except:
            #     pass

            row_dict = { 'link': link, 'title': title, 'date': date }
            result_map = result_map.append([row_dict])
        
        # try:
        #     WebDriverWait(driver, 1).until(element_to_be_clickable((By.ID, "finaprofessional"))).click()
        #     WebDriverWait(driver, 1).until(element_to_be_clickable((By.ID, "_evidon-accept-button"))).click()
        # except:
        #     print('no login needed')

        try:
            wait.until(element_to_be_clickable((By.ID, "ctl00_ctl00_MainContent_Layout_1MainContent_lnkNextPage"))).click()
        except:
            try:
                WebDriverWait(driver, 5).until(element_to_be_clickable((By.ID, "finaprofessional"))).click()
                WebDriverWait(driver, 1).until(element_to_be_clickable((By.ID, "_evidon-accept-button"))).click()
                wait.until(element_to_be_clickable((By.ID, "ctl00_ctl00_MainContent_Layout_1MainContent_lnkNextPage"))).click()
                print('logging in')
            except:
                print('no login needed')
                wait.until(element_to_be_clickable((By.ID, "ctl00_ctl00_MainContent_Layout_1MainContent_lnkNextPage"))).click()


result_map.to_csv('morningstar_map.csv')