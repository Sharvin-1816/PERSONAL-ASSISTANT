import webbrowser
import requests
from bs4 import BeautifulSoup

url_inshorts = 'https://inshorts.com/en/read'
url_hindustantimes = 'https://timesofindia.indiatimes.com/briefs'

r1 = requests.get(url_inshorts)

soup_object1 = BeautifulSoup(r1.text , 'html.parser')

# file  = open("f.txt",'a')

a=soup_object1.prettify()
for div in soup_object1.findAll('div', attrs={'class':'KkupEonoVHxNv4A_D7UG'}):
    txt = div.text
    # file.write(div.text)
    print(div.text)
    print("------------------------------------------------------------------------------------------------")

r2 = requests.get(url_hindustantimes)

soup_object2 = BeautifulSoup(r2.text,'html.parser')

b=soup_object2.prettify()
for div in soup_object2.findAll('div', attrs={'class':'brief_box'}):
    txt = div.text
    print(div.text)
    print("------------------------------------------------------------------------------------------------")
