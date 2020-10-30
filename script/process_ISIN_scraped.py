import datetime
import time
import os
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


data = pd.read_csv("isin_scraped.csv")



print(data['content'].describe())