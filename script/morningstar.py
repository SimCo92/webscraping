from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import presence_of_element_located

# import requests
import datetime
import os
# from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

date = str(datetime.date.today())


LINK = 'https://www.morningstar.it/'

path = os.getcwd() + '/chromedriver'
driver = webdriver.Chrome(path)
# driver = webdriver.Firefox()
driver = driver.get(LINK)


driver.find_element_by_id()

# result = driver.find_element_by_id("finaprofessional").click()

# driver = driver.find_element_by_id('ctl00_ctl00_MainContent_Layout_1MainContent_lnkNextPage').click()

# for n in range(1,13):
# # for n in range(1,3):
#     LINKn = LINK + str(n)
#     response = requests.get(LINKn)
#     print(LINKn)
#     soup = BeautifulSoup(response.text, 'html.parser')cd
#     raw = soup.findAll("li", {"class": "list-lined-item"})
#     resultxpage = len(raw)
#     for i in range(resultxpage):
#         text = raw[i].text
#         meta = raw[i].findAll("a", {"class": "meta-part"})
#         title = raw[i].findAll("h3", {"class": "aprev-title"})[0].text
#         link = 'www.ilsole24ore.com' + meta[0]['href']
#         topic = meta[0].text
#         # result_map = pd.DataFrame(np.array([link, topic, title]), columns=['link', 'topic', 'title'])