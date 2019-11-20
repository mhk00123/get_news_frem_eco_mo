from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import os

payload = {
    '_username': 'cpttm',
    '_password': 'cpttm2admin',
    '_remember_me': True,
    '_csrf_token': '',
}

link = 'http://www.sme360.mo/admintools/login'

browser = webdriver.Chrome()

# Clean All Cookie first
browser.delete_all_cookies()

browser.get(link)

# now_handle = browser.current_window_handle

# print(now_handle.text)

browser.quit()