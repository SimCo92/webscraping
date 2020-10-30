from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, presence_of_element_located

import datetime
import time
from bs4 import BeautifulSoup
import pandas as pd

def get_ISIN_webpage(driver, links, outputname='isin_scraped'):
    """
    accetta un webdriver una lista python di link morningstar e il nome del file di output.
    => restituisce un file
    """
    content_df = pd.DataFrame()
    content_dict = {}
    with driver:
        for index, link_isin in enumerate(links):
            if link_isin == 'missing':
                content_dict = { 'link': link_isin, 'content' : none }
            else:
                print('processing : ', link_isin)
                driver.get(str('https://www.morningstar.it' + link_isin)) 
                driver = clickpopup(driver)
                wait = WebDriverWait(driver, 5)
                wait.until(presence_of_element_located((By.ID, "mainContentDiv")))
                try:
                    tableoverview = wait.until(presence_of_element_located((By.CLASS_NAME, "overviewPortfolioMixTable")))
                    print('table found')
                    table_html = BeautifulSoup(tableoverview.get_attribute('innerHTML'), 'html.parser')
                except:
                    table_html = None
                    print('no table')
                content_dict = { 'link': link_isin, 'content' : table_html }

            content_df = content_df.append([content_dict])
            print('articles processed : ', index)
    return content_df.to_csv(str(outputname) + '.csv')



def clickpopup(driver):
    """
    Se presente risolve il popup di morningstar
    """
    wait = WebDriverWait(driver, 5)
    try:
        WebDriverWait(driver, 5).until(element_to_be_clickable((By.ID, "finaprofessional"))).click()
        WebDriverWait(driver, 1).until(element_to_be_clickable((By.ID, "_evidon-accept-button"))).click()
        print('logging in')
    except:
        print('no login needed')
    return driver