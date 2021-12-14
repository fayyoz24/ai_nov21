import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd

url = 'https://www.youtube.com/watch?v=JdWzEXb_iM8'
#pth = "chromedriver.exe"
#driver = webdriver.Chrome(pth)

driver = webdriver.Chrome(executable_path='C:\programexe\chromedriver.exe')
driver.get(url)
video = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[1]/video')
print(video.text)