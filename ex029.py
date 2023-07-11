velocidade = int(input('Quantos kilômetros por hora o carrou ultrapassou os 80km/h no radar? Insira a quantidade à mais:'))
radar = velocidade * 7
if velocidade > 0:
    print('Você foi multado por estar andando à {}km/h em uma pista de 80km/h! E por cada kilômetro a mais'
          ' de velocidade, você terá de pagar R$7,00 ... '
          'No total você pagará R${:.2f}'.format(velocidade + 80, radar))
else:
    print('Você está dirigindo corretamente conforme a regra de velocidade desta estrada. :)')
