import get_html
from collections import OrderedDict
import json 

link = 'https://www.economia.gov.mo/zh_TW/web/public/pg_nc_wn'
css  = 'div div table tbody tr td'

# python有序字典
dic = OrderedDict()

p_date  = []
p_title = []

def get_ECO():
    result = get_html.html_get(link, css)
    for i in range(2, len(result)-1):
        if(i%2 == 0):
            p_date.append(result[i].text)
            # print(result[i].text)

        elif(i%2 == 1):
            p_title.append(result[i].text)
            # print(result[i].text)

    for i in range(0, len(p_date)):
        dic[p_title[i]] = p_date[i]
    
    json_dic = json.dumps(dic)
    # print(json_dic)
    return json_dic