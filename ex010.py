nome = str(input('Olá, como você se chama? '))
print('Seja bem-vindo {}!'.format(nome))
dinheiro = float(input('Quantos R$ você tem na sua carteira? R$'))
print('Com R${:.2f}, você terá ${:.2f} e £{:.2f}!'.format(dinheiro, dinheiro / 4.86, dinheiro / 5.28))
