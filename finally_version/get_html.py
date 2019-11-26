from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time


def html_get(link, css_locate):
    print("------HTML Get------")
    # 選用Chrome
    browser = webdriver.Chrome()
    # Clean All Cookie first
    browser.delete_all_cookies()
    # Get Link
    browser.get(link)
    time.sleep(1)
    html = browser.find_elements_by_css_selector(css_locate)
    time.sleep(1)
    # browser.quit()
    return html