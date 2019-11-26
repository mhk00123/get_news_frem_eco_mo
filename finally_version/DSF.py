import get_html
from collections import OrderedDict
import json 

link = 'https://www.dsf.gov.mo/xml/RSS_Taxation_Info_C.xml'
css  = 'table tbody tr td'

# python有序字典
dic = OrderedDict()

p_date  = []
p_title = []

def get_DSF():
    result = get_html.html_get(link, css)
    for i in range(0, len(result)):
        if(i == 0):
            p_title.append(result[i].text)
            # print(result[i].text)
        elif(i%2 == 1):
            p_date.append(result[i].text)
            # print(result[i].text)
        elif(i%2 == 0):
            p_title.append(result[i].text)
            # print(result[i].text)
    
    for i in range(0, len(p_date)):
        dic[p_title[i]] = p_date[i]

    json_dic = json.dumps(dic)
    # print(json_dic)
    return json_dic