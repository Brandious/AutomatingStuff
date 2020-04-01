import requests
from bs4 import BeautifulSoup
import re
import json 
import sys

URL =  'https://olx.ba'

page = requests.get(URL)
page.raise_for_status()
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id = 'rezultatipretrage')

art_elems = results.find_all('div', class_= 'artikal')


print(art_elems)

f = open('test.json',  'w')

list = []

for  art in art_elems: 
        try:
            title_elem = art.find('div', class_='naslov') 
            if title_elem is None: continue
        
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
        except: 
            print('dosta je')
            break
     
       

print(len(list));
f.write(json.dumps(list))

f.close()

