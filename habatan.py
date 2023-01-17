import requests,sys,re
from bs4 import BeautifulSoup
#url = "https://hyogo-de-tabeyou.com/search?areas%5B0%5D=1&page=85"
#r= requests.get(url)
#soup = BeautifulSoup(r.content, "html.parser")
soup = BeautifulSoup(open(sys.argv[1]), "html.parser")
elem = soup.select("#contents > div.c-yellow-bg-zone > div > div > div.shop-list-wrap")
#elem = soup.select("#contents > div.c-yellow-bg-zone > div > div > div.shop-list-wrap > div:nth-child(2) > div.shop-list-ttl")
shop = soup.find_all(class_='shop-list-ttl')
addr = soup.find_all(class_='shop-list-address')
tel = soup.find_all(class_='shop-list-tel')
j=0
for i in shop:
    s = addr[j].text.replace('\n','')
    s=re.sub(' +', ' ', s).strip(' ')
    print(i.text,',',s,',',tel[j].text.strip('TEL: '),sep='')
    j = j + 1

#print(elem)
#print(r.headers)
#print(r.content)
