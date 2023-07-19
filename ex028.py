import random, emoji, time
# I have imported 3 libraries, to create a program that will make the computer "think on a number" then ask the user ...
# what kind of number he thinks the computer thought. If the user wins, the it will say "You won blá blá", if not, "oh noes"
'''numeros = [0, 1, 2, 3, 4, 5]

comp = (random.choice(numeros))

user = int(input('Entre os números de 0 à 5, qual você acha que o computador escolheu? '))

if user == comp:
    print('Você acertou, mas que sortudo!')
else:
    print('Deu mole, você errou!')
print('O computador escolheu ... ', comp)'''
print('')
# 'Here is the best version and with less codelines ( and also more cool!', emoji.emojize('nerd_face:')
computer = random.randint(0, 5)

print('Estou pensando ...'.upper())

time.sleep(2)

pensador = int(input('Qual número você acha que o computador pensou? '))

print(emoji.emojize(':neutral_face:'), '...')

time.sleep(1)

if pensador == computer:
    print(emoji.emojize(':angry_face:'), '\033[1;33mParabéns\033[m, \033[32mvocê acertou\033[m o número do computador!')
else:
    print('Ih ... \033[31mVocê errou\033[m! O computador pensou no número \033[34m{}\033[m.'.format(computer)
          + emoji.emojize(':backhand_index_pointing_up:' + ':nerd_face:'))
