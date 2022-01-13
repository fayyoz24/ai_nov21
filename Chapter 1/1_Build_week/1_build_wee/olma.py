import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd
from selenium.webdriver.chrome.options import Options
import re
import math
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


data = pd.read_csv('books.csv')
urls = data['Urls']
awards203 = [] #str
awards306 = []

for url in urls[:2]:
    driver = webdriver.Chrome(executable_path='C:\programexe\chromedriver.exe')
    driver.get(url)
    
    try:
      more_detail = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div[2]/div[4]/div[1]/div[2]/div[5]/div[3]/a[1]')
      more_detail.click()                       #/html/body/div[1]/div[1]/main/div[1]/div[2]/div[3]/div[6]/div/div/button/span
                        
    except NoSuchElementException:
      pass
    
    try:
      more_details = driver.find_element_by_xpath('/html/body/div[1]/div[1]/main/div[1]/div[2]/div[3]/div[6]/div/div/button/span')
      driver.execute_script("arguments[0].click();", more_details)
      more_details.click()    
      driver.implicitly_wait(10)                   #/html/body/div[2]/div[3]/div[1]/div[2]/div[4]/div[1]/div[2]/div[5]/div[3]/a[1]
    except (NoSuchElementException, ElementNotInteractableException):
      pass
    try:
      more = driver.find_elements_by_class_name('toggleLink')
      for c in more:
          c.click()
      #driver.execute_script("arguments[0].click();", more:
    except (NoSuchElementException, IndexError):
      pass                    

    temp_award = []
    a = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div[2]/div[4]/div[1]/div[2]/div[5]/div[3]/div[1]').text
    awards306.append([a])
    df = pd.DataFrame({'awards': awards306})
    df.to_csv('award.csv')
    driver.close()


    print(awards306)