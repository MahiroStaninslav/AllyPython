import requests
from bs4 import BeautifulSoup as sopa
linkDOL = 'https://www.google.com/search?q=cotação+dólar'
headersDOL = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0'}
requisitionDOL = requests.get(linkDOL, headers=headersDOL)
siteDOL = sopa(requisitionDOL.text, 'html.parser')

dólar = siteDOL.find('span', class_='DFlfde SwHCTb')
preçodólar = dólar.get_text()
preçodólar = preçodólar.replace(',', '.')
doleta = float(preçodólar)

linkEUR = 'https://www.google.com/search?q=cotação+euro'
headersEUR = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0'}
requisitionEUR = requests.get(linkEUR, headers=headersEUR)
siteEUR = sopa(requisitionEUR.text, 'html.parser')

euro = siteEUR.find('span', class_='DFlfde SwHCTb')
preçoeuro = euro.get_text()
preçoeuro = preçoeuro.replace(',', '.')
eurovski = float(preçoeuro)

linkDEUR = 'https://www.google.com/search?q=cotação+dólar+para+euro'
headersDEUR = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0'}
requisitionDEUR = requests.get(linkDEUR, headers=headersDEUR)
siteDEUR = sopa(requisitionDEUR.text, 'html.parser')

DolEur = siteDEUR.find('span', class_='DFlfde SwHCTb')
preçoDEUR = DolEur.get_text()
preçoDEUR = preçoDEUR.replace(',', '.')
DEUR = float(preçoDEUR)

nome = str(input('Olá, seja bem-vindo(a), como é o seu nome? ')).strip()
print('')
print('Será um prazer poder te ajudar, {}!'.format(nome))
print('')
moeda = int(input('Primeiro, escolha qual o tipo de moeda, digite [ 1 ] para Real, [ 2 ] para Dólar ou [ 3 ] para Euro: '))
print('')
if moeda == 1:
    reais = float(input('Quantos Reais você quer ver quanto valeria nas outras duas moedas? R$'))
    print('')
    print('Em \033[34mDólares\033[m valerá: \033[34m${:.2f}\033[m'.format(reais / doleta))
    print('')
    print('Em \033[33mEuros\033[m valerá: \033[33m£{:.2f}\033[m'.format(reais / eurovski))
elif moeda == 2:
    dólares = float(input('Quantos Dólares você quer ver quanto valeria nas outras duas moedas? $'))
    print('')
    print('Em \033[32mReais\033[m valerá: \033[32mR${:.2f}\033[m'.format(dólares * doleta))
    print('')
    print('Em \033[33mEuros\033[m valerá: \033[33m£{:.2f}\033[m'.format(dólares * DEUR))
elif moeda == 3:
    Euros = float(input('Quantos Euros você quer ver quanto valeria nas outras duas moedas? £'))
    print('')
    print('Em \033[32mReais\033[m valerá: \033[32m{:.2f}\033[m'.format(Euros * eurovski))
    print('')
    print('Em \033[34mDólares\033[m valerá: \033[34m{:.2f}\033[m'.format(Euros / DEUR))
else:
    print('Você digitou o número errado, por favor, selecione a numeração de um dos três!')
print('')
print('\033[36;40mFoi um prazer te ajudar, Senhor(a) {}!\033[m'.format(nome))
