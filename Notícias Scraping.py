import requests
from bs4 import BeautifulSoup

url = 'https://jovemnerd.com.br/nerdbunker/gen-v-ganha-data-de-estreia-no-prime-video/'

response = requests.get(url)
print('Aqui está o Código de Status!', response.status_code)
content = response.content
print('')

site = BeautifulSoup(content, 'html.parser')
print(type(site))
print('')

News = site.find('header', attrs={'class': "header"})
# print(Title.prettify())
# <h1 class="title"> e <p class="excerpt">

TitleR = News.find('h1', attrs={'class': "title"})

SubTitle = News.find('p', attrs={'class': "excerpt"})
print(TitleR.text)
print(SubTitle.text)
print('')

conteudo = site.find('div', attrs={'class': "content-left"})
# print(conteudo.prettify())

contnews = conteudo.find_all('p')
for p in contnews:
    text_contnews = p.get_text()
    print(text_contnews)
