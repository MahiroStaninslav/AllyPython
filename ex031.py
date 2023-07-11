viagem = int(input('Quantos kilômetros de distância terá essa viagem? km'))
passagem1 = viagem * 0.50
passagem2 = viagem * 0.45
if viagem <= 200:
    print('Sua viagem de {} kilômetros, por ter 50 centavos por cada km, pagará no total R${:.2f}!'.format(viagem, passagem1))
else:
    print('Sua viagem de {} kilômetros, por ter passado dos 200 km, você pagará 45 centavos por cada km, no total R${:.2f}!'.format(viagem, passagem2))
print('Boa Viagem!'.upper())
