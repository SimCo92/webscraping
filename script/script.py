import datetime
import time
import os
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from morningstar_utils import clickpopup, get_ISIN_webpage

date = str(datetime.date.today())
path = os.getcwd() + '/chromedriver'
driver = webdriver.Chrome(path)

data = pd.read_csv("isin_map.csv")
links = data['link']

get_ISIN_webpage(driver, links, outputname='isin_scraped')