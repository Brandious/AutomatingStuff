from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options 
import re
import json 

URL =  'https://olx.ba'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id = 'rezultatipretrage')

art_elems = results.find_all('div', class_= 'artikal')


print(len(art_elems)) #stringovi

f = open('test.json',  'w')

list = []

for  art in art_elems: 
        title_elem = art.find('div', class_='naslov') 
        if title_elem is None: break
       
        title = title_elem.find('p', class_='na')
    
        tip = title_elem.find('div', class_='pna')
        
        slika_elem = art.find('div', class_='slika')
        slika = slika_elem['data-malaslika']

        cijena_elem = art.find('div', class_='cijena')
        cijena = cijena_elem.find('div', class_='datum')

        obj = {
            "title" : title.text.strip(),
            "slika": slika,
            "tip": tip.text.strip(),
            "cijena": cijena.find('span').text.strip()
        }
       
        list.append(obj)
     
       

print(list)        
f.write(json.dumps(list))

print(len(list))
f.close()