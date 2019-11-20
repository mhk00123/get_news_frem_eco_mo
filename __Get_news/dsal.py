import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# driver = webdriver.Chrome()

link = 'https://www.dsal.gov.mo/zh_tw/text/index_news.html'

my_headers = {
            'Accept' : '*/*',
            'X-Requested-With' : 'XMLHttpRequest',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
            'Sec-Fetch-Site' : 'same-origin',
            'Sec-Fetch-Mode' : 'cors',
            'Referer' : 'https://www.dsal.gov.mo/zh_tw/text/index_news.html',
            'Accept-Encoding' : 'gzip, deflate, br',
            'Accept-Language' : 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cookie' : 'JSESSIONID=F7D4361C0DC83B9B13079DE4CF270829'
        }

result = requests.get(link, headers=my_headers)

content = result.text
soup = BeautifulSoup(content, 'html.parser')

print(soup)