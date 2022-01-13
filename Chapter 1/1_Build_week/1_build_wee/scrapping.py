import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd
urls = [] #str

titles = [] #str
authors = [] #str
num_reviews = [] #int
num_ratings = [] #int
avg_rating = []  #float
or_pub_year = [] #int
genres = [] # 3 str
awards = [] #str
places = [] #str
page = [2]
for j in page:
    url = 'https://www.goodreads.com/list/show/1.Best_Books_Ever?page='+str(j)
    driver = webdriver.Chrome(executable_path='C:\programexe\chromedriver.exe')
    # driver.implicitly_wait(20)
    for i in range(1, 101):
        # vote = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div[2]/div[3]/div[5]/table/tbody/tr['+str(i)+']/td[3]/div[2]/span/a[2]').text
        # vote = int(re.sub(r'\D', '', vote))
        # num_votes.append(vote)

        # rating = driver.find_element_by_xpath('//*[@id="all_votes"]/table/tbody/tr['+str(i)+']/td[3]/div[1]/span/span').text
        # rating = re.findall(r"[-+]?\d*\.\d+|\d+", rating)
        # num_rat = ''
        # for x in rating[1:]:
        #     num_rat+=x
        # num_ratings.append(int(num_rat))

        # avg_rating.append(float(rating[0]))                                          

        # review = driver.find_element_by_xpath('//*[@id="all_votes"]/table/tbody/tr['+str(i)+']/td[3]/div[2]/span/a[1]').text
        # review = int(re.sub(r'\D', '', review))
        # num_reviews.append(review)                                        
        
        # author = driver.find_element_by_xpath('//*[@id="all_votes"]/table/tbody/tr['+str(i)+']/td[3]/span[2]/div/a/span').text
        # authors.append(author)  
                                        
        title = driver.find_element_by_xpath('//*[@id="all_votes"]/table/tbody/tr['+str(i)+']/td[3]/a/span').text                           
        titles.append(title)





# # for i in range(1, 1001):
# url = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div[2]/div[3]/div[5]/table/tbody/tr[1]/td[3]/a')
# print(url.text)