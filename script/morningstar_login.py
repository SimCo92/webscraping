from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, presence_of_element_located, frame_to_be_available_and_switch_to_it, presence_of_all_elements_located

from  morningstar_utils import clickpopup
import time
import os
from bs4 import BeautifulSoup
import pandas as pd

LINK = 'https://www.morningstar.it'
mail = 'mauromartelli600@gmail.com'
pw = 'CapUni03'
pathchrome = os.getcwd() + '/chromedriver'
path = os.getcwd()

# date = str(datetime.date.today())
result_map = pd.DataFrame()

# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized");
# options.add_argument("disable-infobars")
# options.add_argument("--disable-extensions")

def login():

    with webdriver.Firefox(path) as driver:
    # with webdriver.Chrome(pathchrome) as driver:
        wait = WebDriverWait(driver, 20)
        
        driver.get(LINK)
        time.sleep(10)

        clickpopup(driver)

        # login
        time.sleep(5)
        wait.until(element_to_be_clickable((By.ID, "lnkLoginNew"))).click()
        wait.until(frame_to_be_available_and_switch_to_it("frameContainer"))

        form = wait.until(presence_of_element_located((By.CSS_SELECTOR, "form")))
        wait.until(presence_of_element_located((By.ID, "txtUsername"))).send_keys(mail)
        wait.until(presence_of_element_located((By.ID, 'txtRealPassword'))).click()
        # .send_keys(pw)
        time.sleep(5)

        return driver

driver = login()

# LINK2 = 'https://www.morningstar.it/it/collection/3003/3104/news-fondi.aspx'
# driver.get(LINK2)
# time.sleep(10)