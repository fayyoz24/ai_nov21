import requests
from bs4 import BeautifulSoup
import pandas as pd


page =requests.get("https://www.imdb.com/list/ls009668711/")


soup = BeautifulSoup(page.content, "html.parser")

#week = soup.find(id="seven-day-forecast-body")
#print(week)
a= soup.findAll("div",class_="lister-item mode-advanced")
print(a[0].text)
#("div",class_="lister-item mode-advanced")
# items = week.find_all(class_="tombstone-container")
# #print(items)


# #items[0].find(class_='period-name').get_text
# #items[0].find(class_='short-desc').get_text
# #items[0].find(class_='temp').get_text

# Period_names = [item.find(class_='period-name').get_text() for item in items]
# Short_descriptions =  [item.find(class_='short-desc').get_text() for item in items]
# Temperature = [item.find(class_='temp').get_text() for item in items]


# weather = pd.DataFrame(
#     {   'Period':Period_names,
#        'Short description':Short_descriptions,
#        'Temperature':Temperature,
#     })
# print(weather)
# weather.to_csv('weather.csv')