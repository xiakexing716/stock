# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 11:49:48 2019

@author: kyy
@function: 爬取东方财富网全球新闻
http://global.eastmoney.com/a/cqqdd_1.html
"""

import requests
from bs4 import BeautifulSoup as bs


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

a = requests.get("http://global.eastmoney.com/a/cqqdd_1.html",headers=headers)

# bs解析
def parseinfo(url):
    html = requests.get(url,headers=headers)
    if html.status_code == 200 and html.text:
        bs0 = bs(html.text,features='lxml')
        bs1 = bs0.find(id='newsListContent')
        bs2 = bs1.find_all('p',class_='title')
        return bs2
    
def parsedetail(url):
    html = requests.get(url,headers=headers)
    rsttext = []
    if html.status_code == 200 and html.text:
        bs0 = bs(html.text,features='lxml')
        bs1 = bs0.find(id='ContentBody')
        bs2 = bs1.find_all('p')
        for i in bs2:
            rsttext.append(i.get_text(strip=True))
        return rsttext
    


if __name__ == '__main__':
#    test = parseinfo('http://global.eastmoney.com/a/cqqdd_1.html')
    test = parsedetail('http://global.eastmoney.com/a/201903281082300969.html')