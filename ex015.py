Diária = int(input('Quantos dias você esteve com o carro alugado? '))

dias = Diária * 60
print('')
print('Se você usar o carro alugado por {} dias, você pagará R${} sem contar os kilômetros.'.format(Diária, dias))

kilom = float(input('Quantos kilômetros você percorreu com o seu carro alugado? km'))

km = kilom * 0.15
print('')
print('Se você percorrer {:.0f} kilômetros, então você pagará R${:.2f} sem contar os dias.'.format(kilom, km))

result = dias + km
print('')
print('O preço do aluguel totalizando, o que você terá de pagar pelo carro alugado vai ser de R${:.2f}!'.format(result))
