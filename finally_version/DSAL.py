import get_html
from collections import OrderedDict
import json 

link = 'https://www.dsal.gov.mo/zh_tw/text/index_news.html'
css  = 'div table tbody tr td'

# python有序字典
dic = OrderedDict()

p_date  = []
p_title = []

def get_DSAL():
    result = get_html.html_get(link, css)
    j = 0
    for i in range(7, len(result)-3):
        # print(result[i].text)
        if(j == 0):
            p_title.append(result[i].text)
        if(j == 1):
            p_date.append(result[i].text)
        if(j == 2):
            j = 0
            continue
        j = j+1

    for i in range(0, len(p_date)):
        dic[p_title[i]] = p_date[i]

    json_dic = json.dumps(dic)
    # print(json_dic)
    return json_dic