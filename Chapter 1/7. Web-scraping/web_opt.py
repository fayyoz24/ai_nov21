import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd

url = 'https://www.youtube.com/watch?v=HUgMWJKn2YY&t=9s'
#pth = "chromedriver.exe"
#driver = webdriver.Chrome(pth)

driver = webdriver.Chrome(executable_path='C:\programexe\chromedriver.exe')
driver.get(url)
driver.maximize_window() # For maximizing window
driver.implicitly_wait(20)
cookies = driver.find_element_by_xpath('/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a/tp-yt-paper-button')
#olma = driver.find_element_by_xpath('/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a/tp-yt-paper-button/yt-formatted-string')
cookies.click()
#driver.implicitly_wait(50)
sleep(5)
pause_play = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[28]/div[2]/div[1]/button')
pause_play.click()
sleep(7)
#print(olma.text)
#'document.querySelector("#text")'
driver.quit()