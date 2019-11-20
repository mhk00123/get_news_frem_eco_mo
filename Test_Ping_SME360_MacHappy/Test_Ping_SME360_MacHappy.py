import requests
import os

link_SME360 = ['https://www.sme360.mo/zh-hant/',
                'https://www.sme360.mo/zh-hant/news',
                'https://www.sme360.mo/zh-hant/book/0/0',
                'https://www.sme360.mo/zh-hant/operation',
                'https://www.sme360.mo/pt/news'] #葡文

link_MacHappy = ['https://macaohappyplay.mo/mobile',
                 'https://macaohappyplay.mo/mobile#!/https://macaohappyplay.mo/mobile/sort/industry_1',
                 'https://macaohappyplay.mo/mobile#!/https://macaohappyplay.mo/mobile/sort/industry_2',
                 'https://macaohappyplay.mo/mobile#!/https://macaohappyplay.mo/mobile/sort/industry_3',
                 'https://macaohappyplay.mo/mobile#!/https://macaohappyplay.mo/mobile/sort/industry_4']

def ping_function(link):
    for i in link:
        result = requests.get(i)
        if(result.status_code == 200):
            print("Success")
        else:
            print("以下連續結無法訪問: " + i)


if __name__ == '__main__':
    ping_function(link_SME360)
    ping_function(link_MacHappy)
    os.system("pause")