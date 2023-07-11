preço = float(input('Qual o preço do produto que você quer consultar? R$'))
desconto = (preço * 5) / 100
total = preço - desconto
print('O seu produto de R${}, com o desconto de 5%, passará a ser R${}!'.format(preço, total))
