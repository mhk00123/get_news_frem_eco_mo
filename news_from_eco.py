# 先尋找已存資料檔 - 上一次執行程式時最新的標題
# 爬取最新資料的第一筆
# 比對新舊2筆標題
# -如有不同 - 使用Webchat API作出通知 / Email

from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

# Load Old File
f = open("old.txt", "r")
log = f.readline()
f.close()

# 經濟局網站
link = "https://www.economia.gov.mo/zh_TW/web/public/pg_nc_wn"

# 使用chrome的webdriver
browser = webdriver.Chrome()

# Clean All Cookie first
browser.delete_all_cookies()
browser.get(link)
time.sleep(2)

# 執行Javascript - 回傳JS渲染的內容
html = browser.execute_script('return document.getElementById("itemsTable").innerHTML')
browser.quit()

text = BeautifulSoup(html, "html.parser")

# 查找所有發佈時間及標題
news = text.find_all("td")

# 第一條新聞(Title)
news = news[1].text

# 比對
if(log == news):
    print("今天沒有新的新聞")

# 發送通知
else:
    print("有更新了")
    ## 記錄Log
    f = open("old.txt", 'w+')
    f.write(news)
    f.close()

    ## 使用WeChat通知
    data = {'text' : "經濟局有新聞更新啦a", 'desp' : news}
    requests.post('https://sc.ftqq.com/SCU52896T17559e439d325e78cd0f71bfa5b877945cf68de25a16b.send?', data=data)