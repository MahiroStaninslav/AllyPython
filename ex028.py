import random, emoji
'''numeros = [0, 1, 2, 3, 4, 5]
comp = (random.choice(numeros))
user = int(input('Entre os números de 0 à 5, qual você acha que o computador escolheu? '))
if user == comp:
    print('Você acertou, mas que sortudo!')
else:
    print('Deu mole, você errou!')
print('O computador escolheu ... ', comp)'''
print('')
computer = random.randint(0, 5)
print('Estou pensando ...'.upper())
pensador = int(input('Qual número você acha que o computador pensou? '))
if pensador == computer:
    print(emoji.emojize(':angry_face:'), 'Parabéns, você acertou o número do computador!')
else:
    print('Ih ... Você errou! O computador pensou no número {}.'.format(computer)
          + emoji.emojize(':backhand_index_pointing_up:' + ':nerd_face:'))
