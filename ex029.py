velocidade = float(input('Com quantos Km/h o veículo passou no radar? '))
'''radar = velocidade * 7
if velocidade > 0:
    print('Você foi multado por estar andando à {}km/h em uma pista de 80km/h! E por cada kilômetro a mais'
          ' de velocidade, você terá de pagar R$7,00 ... '
          'No total você pagará R${:.2f}'.format(velocidade + 80, radar))
else:
    print('Você está dirigindo corretamente conforme a regra de velocidade desta estrada. :)')'''
radar1 = (velocidade-80) * 7
if velocidade > 80:
    print('MULTA! Você excedeu o limite de velocidade e agora terá de pagar R${}!'.format(radar1))
else:
    print('Parabéns! Você está dirigindo certinho.')
