from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options 
import re
import json 

URL =  'https://telefonski-imenik.biz/bih/sarajevo/imenik-8973'

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find("ul", {"class": "ContactList"})

#art_elems = results.find_all('div', class_= 'artikal')
r = results.find_all("li", class_='ContactListItem')

print(r)
print(type(r))

for res in r: 
      elem = res.find('h3')
      title = elem.find('a', class_='ListItemTitle')
      print(title['title'])
