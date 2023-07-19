print('\033[33mOlá, Seja bem-vindo!\033[m'.upper())
print('')
ValorCasa = int(input('Quanto é o valor da casa? R$'))
print('')
Salário = float(input('Quanto é o salário do comprador? R$'))
print('')
Anospag = int(input('Quantos anos ele vai pagar pela casa? '))
print('')

porcentagem = (Salário * 30) / 100
Prestação = ValorCasa / (Anospag * 12)
# print(porcentagem, Prestação)
if Prestação > porcentagem:
    print('O seu empréstimo bancário foi negado, pois a prestação mensal vai ser \033[31mmaior do que o limite'
          ' aceito\033[m baseado em seu salário de R${:.2f}.'.format(Salário))
    print('O limite não pode exceder 30% do seu salário, \033[33mou seja: R${:.2f}\033[m.'
          ' \033[31mA prestação Mensal ficou R${:.2f}!\033[m'.format(porcentagem, Prestação))
else:
    print('O seu empréstimo bancário \033[32matendeu os requisitos necessários\033[m e foi aceito!')
    print('O limite não poderia exceder 30% do seu salário, \033[33mo que equivale à R${:.2f}\033[m,'
          ' \033[32me a prestação mensal ficou R${:.2f}!\033[m'.format(porcentagem, Prestação))
