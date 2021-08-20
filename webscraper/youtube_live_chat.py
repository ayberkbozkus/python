from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def youtube(url):
    browser = webdriver.Chrome(executable_path='./drivers/chromedriver')
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    messages = soup.find_all("yt-live-chat-text-message-renderer")
    for message in messages:
        content = message.find("div",{"id":"content"})
        author = message.find("span",{"id":"author-name"}).text
        message = content.find("span",{"id":"message"}).text
        space = "#"*20
        print(f'{author} : {message} \n {space}')

print('Enter youtube live chat url:')
url = input()
youtube(url)