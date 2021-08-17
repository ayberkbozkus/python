from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(executable_path='./drivers/chromedriver')
browser.get("http://www.google.com")
input = browser.find_element_by_css_selector(".gLFyf.gsfi")
input.send_keys("twitter deep learning türkiye")
input.send_keys(Keys.ENTER)

click = browser.find_element_by_css_selector(".LC20lb.DKV0Md")
click.click()

pageSource = browser.page_source

page_soup = BeautifulSoup(pageSource, 'html.parser')

tweets = page_soup.find_all("div", attrs={"data-testid":"tweet"})

print(tweets)
print(type(tweets))

for tweet in tweets:
    print(tweet.find("div",attrs={"class":"css-901oao r-1fmj7o5 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"}).text)