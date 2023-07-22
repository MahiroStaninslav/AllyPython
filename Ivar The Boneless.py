import requests
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/Ivar_the_Boneless'
response = requests.get(url)
site = BeautifulSoup(response.content, 'html.parser')

print(response.status_code)

Title = site.find('span', attrs={'class': "mw-page-title-main"})
print(Title.text)
print('')
HistoryOutput = site.find('div', attrs={'class': "mw-parser-output"})

HistoryContent = HistoryOutput.find_all('p')
HistoryNonListed = HistoryOutput.find_all('ul')

for p in HistoryContent:
    text_HC = p.get_text()
    print(text_HC)

for ul in HistoryNonListed:
    listNL_HNL = ul.find_all('li')
    for li in listNL_HNL:
        text_HNL = li.get_text()
        print('°', text_HNL)
