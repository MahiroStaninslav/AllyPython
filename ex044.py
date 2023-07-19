produto = float(input('Qual o valor do produto? R$'))
MPagamento = str(input('Qual será a forma do pagamento, à vista ou parcelado? ')).strip()
if MPagamento.lower() in ['à vista']:
    MPagamento = str(input('Você vai pagar no dinheiro/cheque ou no cartão? ')).strip()
    if MPagamento.lower() in ['Dinheiro/Cheque' or 'Dinheiro']:
        print('O valor total do produto ao ser pago à vista com o dinheiro, vai ficar R${:.2f}!'.format(produto - ((produto * 10)/100)))
    elif MPagamento.lower() in ['Cartão']:
        print('O valor total do produto ao ser pago à vista com o cartão, vai ficar R${:.2f}!'.format(produto - ((produto * 5)/100)))

elif MPagamento.lower() in ['parcelado']:
    MPagamento = str(input('Em quantas vezes você vai parcelar? ')).strip()
    if MPagamento.lower() in ['2x']:
        print('O valor total à ser pago em 2 vezes na parcela, vai ficar R${:.2f}, e as parcelas serão R${:.2f}'.format(produto, produto / 2))
    elif MPagamento.lower() == '3x' or '4x' or '5x' or '6x' or '7x' or '8x' or '9x' or '10x':
        print('O valor total à ser pago em 3x ou mais parcelas, vai ficar R${:.2f} com 20% de juros!'.format(produto + ((produto * 20)/100)))
