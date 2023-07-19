dolar = float(4.80)
euro = float(5.26)
yuan = float(0.66)
rublo = float(0.05)
iene = float(0.03)

colors = {"blue": '\033[34m', "red": '\033[31m', "yellow": '\033[33m',
           "green": '\033[32m', "purple": '\033[35m', "clear": '\033[m'}

print('O preço do {}Dólar{} (US$) está {}{:.2f}{}R$!'.format(colors["blue"], colors["clear"], colors["blue"], dolar, colors["clear"]))
print('O preço do {}Euro{} (EUR) está {}{:.2f}{}R$!'.format(colors["yellow"], colors["clear"], colors["yellow"], euro, colors["clear"]))
print('O preço do {}Yuan Chinês{} (CNY) está {}{:.2f}{}R$!'.format(colors["red"], colors["clear"], colors["red"], yuan, colors["clear"]))
print('O preço do {}Rublo Russo{} (RUB) está {}{:.2f}{}R$!'.format(colors["green"], colors["clear"], colors["green"], rublo, colors["clear"]))
print('O preço do {}Iene Japonês{} (JPY) está {}{:.2f}{}R$!'.format(colors["purple"], colors["clear"], colors["purple"], iene, colors["clear"]))

reais = int(input('Quantos Reais você tem na carteira disponíveis? '))
RD = reais / dolar
RE = reais / euro
RY = reais / yuan
RR = reais / rublo
RI = reais / iene

print('Com \033[1;33m{}R$\033[m, você terá esta quantidade em outras moedas: '
      '{}US${} = {}{:.2f}{} // {}EUR{} = {}{:.2f}{} // '
      '{}CNY{} = {}{:.2f}{} // {}RUB{} = {}{:.2f}{} // {}JPY{} = {}{:.2f}{}'.format(reais, colors["blue"], colors["clear"], colors["blue"], RD, colors["clear"],
                                                                                    colors["yellow"], colors["clear"], colors["yellow"], RE, colors["clear"],
                                                                                    colors["red"], colors["clear"], colors["red"], RY, colors["clear"],
                                                                                    colors["green"], colors["clear"], colors["green"], RR, colors["clear"],
                                                                                    colors["purple"], colors["clear"], colors["purple"], RI, colors["clear"]))
# 'Here, I have created a program that will calculate your R$ and how much you would have in other currency!'
