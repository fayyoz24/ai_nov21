import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd

url = 'https://weather.com/weather/tenday/l/San+Francisco+CA?canonicalCityId=dfdaba8cbe3a4d12a8796e1f7b1ccc7174b4b0a2d5ddb1c8566ae9f154fa638c'
#pth = "chromedriver.exe"
#driver = webdriver.Chrome(pth)

driver = webdriver.Chrome(executable_path='C:\programexe\chromedriver.exe')
driver.get(url)
days = []
temp_day=[]
temp_night = []
descp_day = []
descp_night = []

for i in range(1, 11):
   tempday = driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details['+str(i)+']/div/div[1]/div/div[1]/span')
   temp_day.append(str(round((int(tempday.get_attribute("textContent").strip("°"))-32)/1.8, 1))+"°C")  
print(temp_day)

for i in range(1,11):
    tempnight = driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details['+str(i)+']/div/div[3]/div/div[1]/span')
                                          
    temp_night.append((str(round((int(tempnight.get_attribute("textContent").strip("°"))-32)/1.8, 1))+"°C"))
print(temp_night)

for i in range(0, 10):
    descpday = driver.find_element_by_css_selector('#detailIndex'+str(i)+' > div > div:nth-child(1) > p')
                                                    #/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[15]/div/div[1]/p
                                                    ##detailIndex14 > div > div:nth-child(1) > p
    descp_day.append(descpday.get_attribute("textContent"))

for i in range(0, 10):
    descpnight = driver.find_element_by_css_selector('#detailIndex'+str(i)+' > div > div:nth-child(3) > p')
    descp_night.append(descpnight.get_attribute("textContent"))



sleep(5)

date = pd.date_range('today', periods=10,
                     freq='D')
data = {
    #"days": [],
    "temperatura/DAY": temp_day,
    "temperatura/NIGHT":temp_night,
    "Description/DAY":descp_day,
    "Description/Night":descp_night
}
pr=pd.DataFrame(data,index=pd.date_range('today', periods=10, freq='D'))

pr.to_csv("olma.csv", index=False)