from bs4 import BeautifulSoup as Sopa
import requests

URL = 'https://kimetsu-no-yaiba.fandom.com/pt-br/wiki/Respiração_do_Sol'
Headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0'}
Requisition = (requests.get(URL, headers=Headers))
Website = Sopa(Requisition.text, "html.parser")
textin = Sopa.prettify(Website)
print(textin)

Titles = Website.find_all('h1')
print(Titles)
print('')
for title in Titles:
    print(title.text)
    print('')
SubTitles = Website.find_all('h2')
print(SubTitles)
print('')
for title in SubTitles:
    print(title.text)
