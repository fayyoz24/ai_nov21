import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

url = 'https://forecast.weather.gov/MapClick.php?x=276&y=148&site=lox&zmx=&zmy=&map_x=276&map_y=148#.Ya8tv9DMLIV'
pth = "chromedriver.exe"
driver = webdriver.Chrome(pth)
driver.get(url)