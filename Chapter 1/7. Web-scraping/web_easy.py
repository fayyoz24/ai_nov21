import math
import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://forecast.weather.gov/MapClick.php?x=276&y=148&site=lox&zmx=&zmy=&map_x=276&map_y=148#.Ya8bLdDMLIU'
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
# temp = soup.find('p', class_ = 'myforecast-current-lrg')
# print(temp.text)
# div = soup.find_all('div', id = 'current-conditions-body')
# ps = div[0].find_all('p')

"""Extract the 5 days, day and night (10 entries) of weather from Los Angeles in weather.gov.
inspect with the console
write code to target the right elements of the text
For each day, you need to store:
The day of the week (Tuesday)
The date (28/09/2020)
A short description of the conditions (Clear early then increasing cloudiness after midnight. Low 41F. Winds light and variable)
The temperature low and high, with a function of your own to convert into Celsius
Save all of this into a Pandas dataframe"""
"""<p class="temp temp-low">Low: 52 °F</p>"""
#print(page)
# for p in ps:
#     print(p.text)
data = soup.find_all('div', id = 'seven-day-forecast-body')
pw = soup.find('p', class_='period-name')
lowtemp = soup.find_all('p', class_='temp temp-low')
# for pw in data:
#     print(pw.text)
# for temp in data:

hightemp = soup.find_all('p', class_= 'temp temp-high')
temp = []
try:
    for i in range(5):
        temp.append("High:" + str((int((hightemp[i].text.strip("High:, °F")))-32)/1.8)+" °C")
        temp.append("Low:" + str((int((lowtemp[i].text.strip("Low:, °F")))-32)/1.8)+" °C")
except IndexError:
    print("")
    
short_desc = []
shortdesc = soup.find_all('p', class_ = 'short-desc')
for i in range(9):
    short_desc.append(shortdesc[i].text)
period_name = []
period = soup.find_all('p', class_ = 'period-name')
for i in range(9):
    period_name.append(period[i].text)
olma = {
    "temperatura": temp,
    "description": short_desc

}
data = pd.DataFrame(olma, index=period_name)
print(data)
