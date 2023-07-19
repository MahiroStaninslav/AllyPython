num = int(input('Digite um número qualquer para ver se ele é par ou ímpar: '))
difer = num % 2
if difer == 0:
    print('O seu número {} é par!'.format(num))
else:
    print('O seu número {} é ímpar!'.format(num))
