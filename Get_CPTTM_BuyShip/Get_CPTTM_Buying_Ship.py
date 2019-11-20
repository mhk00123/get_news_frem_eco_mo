import requests
from bs4 import BeautifulSoup
import re
import xlrd
import os

link = 'https://cms.cpttm.org.mo/index.php?option=com_content&view=article&id=1440&Itemid=1105&lang=zh'

# myfile = requests.get(link)

result = requests.get(link)

soup = BeautifulSoup(result.text, 'html.parser')

r = soup.select('td > p > span > a')

target = r[2].get('href')

target_get = requests.get(target)

# Download File
open('loading.xlsx','wb').write(target_get.content)

# Read File
load_xlsx = xlrd.open_workbook("loading.xlsx")

names = load_xlsx.sheet_names()
worksheet=load_xlsx.sheet_by_index(0)
worksheet_name = load_xlsx.sheet_names()[0]

# 取得行數
nrows = worksheet.nrows
# print(nrows)

for i in range(nrows):
    if(i == 0):
        continue
    for j in worksheet.row_values(i):
        print(j)
    print()

os.system("pause")