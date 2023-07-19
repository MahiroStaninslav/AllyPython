from bs4 import BeautifulSoup
import requests

URL = 'https://kimetsu-no-yaiba.fandom.com/pt-br/wiki/Respiração_do_Sol'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0'}
response = requests.get(URL, headers=headers)
website = BeautifulSoup(response.text, 'html.parser')

Links = website.find_all('a')
for link in Links:
    href = link["href"]
    print(href)
    