ano = int(input('Em qual ano estamos? '))
# Qualquer Ano que seja uniformemente divisível por 4, é um ano bissexto.
# EM um ano bissexto, é acrescentado um dia extra, ficando 366 dias no ano.
# Isto é feito com o objetivo de manter o calendário anual ajustado com a translação da Terra.
# e com os eventos sazonais relacionados às estações do ano.
'''bissexto = ano // 4
resto1 = bissexto % 2
print('O resto da divisão do ano é {}'.format(resto1))
if resto1 == 0:
    print('O Ano Selecionado é um ano bissexto!')
else:
    print('O Ano Selecionado não é um ano bissexto.')

if ano % 4 == 0:
    print('O Ano {} bissexto!'.format(ano))
    if ano % 4 == 2:
        print('O Ano {} bissexto!'.format(ano))
else:
    print('O Ano {} não é bissexto.'.format(ano))'''

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} Bissexto.'.format(ano))
else:
    print('O ano {} não é Bissexto.'.format(ano))
