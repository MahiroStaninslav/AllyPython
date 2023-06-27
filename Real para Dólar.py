dolar = float(4.80)
euro = float(5.26)
yuan = float(0.66)
rublo = float(0.05)
iene = float(0.03)
print('O preço do Dólar (US$) está {}R$!'.format(dolar))
print('O preço do Euro (EUR) está {}R$!'.format(euro))
print('O preço do Yuan Chinês (CNY) está {}R$!'.format(yuan))
print('O preço do Rublo Russo (RUB) está {}R$!'.format(rublo))
print('O preço do Iene Japonês (JPY) está {}R$!'.format(iene))
reais = int(input('Quantos Reais você tem na carteira disponíveis? '))
RD = reais / dolar
RE = reais / euro
RY = reais / yuan
RR = reais / rublo
RI = reais / iene
print('Com {}R$, você terá esta quantidade em outras moedas: US$ = {:.2f} // EUR = {:.2f} // CNY = {:.2f} // RUB = {:.2f} // JPY = {:.2f}'.format(reais, RD, RE, RY, RR, RI))
