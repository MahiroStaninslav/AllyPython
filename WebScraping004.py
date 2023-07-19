from bs4 import BeautifulSoup
import requests
import os

url = 'https://kimetsu-no-yaiba.fandom.com/pt-br/wiki/Respiração_do_Sol'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0'}
requisition = requests.get(url, headers=headers)
site = BeautifulSoup(requisition.text, 'html.parser')

SunBreathing = site.find('div', id='"mw-content-text"', class_="mw-body-content mw-content-ltr")
print(SunBreathing)
