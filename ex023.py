NUM = str(input('Escolha um número entre 1000 à 9999: '))
print('Milhares: {}. \n Centenas: {}. \n Dezenas: {}. \n Unidades: {}.'.format(NUM[0], NUM[1], NUM[2], NUM[3]))
print('*' * 15)
numero = int(input('Digite um número de 0 à 9999: '))
print(f'Analisando seu número {numero} ...')
m = numero // 1000 % 10
c = numero // 100 % 10
d = numero // 10 % 10
u = numero // 1 % 10
print('Você têm: \n Milhar: {}. \n Centena: {}. \n Dezena: {}. \n Unidade: {}.'.format(m, c, d, u))
