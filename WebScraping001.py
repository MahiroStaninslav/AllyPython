import requests
from bs4 import BeautifulSoup as sopa

link1 = "https://www.google.com/search?q=cotação+dólar"
headers1 = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0"}
requisicao1 = requests.get(link1, headers=headers1)
print(requisicao1)
# print(requisicao1.text, 'Este formato de função vai trazer uma resposta em unicode!')
# print(requisicao1.content, 'Este tipo de função, vai trazer a resposta em bytes!')
# print(requisicao1.links, 'Este tipo de função vai trazer os links dos headers!')
# print(requisicao1.url, 'Este tipo de função vai trazer o endereço de pesquisa!')
site = sopa(requisicao1.text, "html.parser")
# print(site.prettify())

# título = (site.find("Title".lower()))
# print(título)

# BarraPesquisa = (site.find_all('input'.lower().strip()))
# print(BarraPesquisa[1])

# barrapesquisa = (site.find(value="cotação dólar"))
# print(barrapesquisa)
# print(barrapesquisa["value"])
dólar = site.find('span', class_="DFlfde SwHCTb")
print(dólar)
print(dólar['data-value'])
print('O preço do dólar está R${}'.format(dólar.get_text()))
