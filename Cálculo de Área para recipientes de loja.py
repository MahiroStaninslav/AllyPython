from time import sleep
nome = str(input('Olá, como o senhor(a) se chama? ')).strip()
print('')
print('\033[1;4mMuito prazer, {}!\033[m'.format(nome))
print('')
sleep(2)
largura = int(input('Qual o tamanho da largura? '))
print('')
altura = int(input('Qual o tamanho da altura? '))
print('')
largura1 = float(input('Qual o tamanho da largura do item no recipiente? '))
print('')
altura1 = float(input('Qual o tamanho da altura do item no recipiente? '))
print('')
área = largura * altura
ração = largura1 * altura1
print('\033[36;40mCalculando dados ...\033[m')
print('')
sleep(2)
print('Seu recipiente tem \033[33m{}x{}m²\033[m, e a sua área mede \033[33m{}m²\033[m.'.format(largura, altura, área))
print('')
print('A área que a sua ração ocupa, equivale à \033[33m{}m²\033[m.'.format(ração))
print('')
unirac = área // ração
print('No seu recipiente de \033[33m{}x{}m²\033[m, terão \033[1;33;40m{:.0f} unidades\033[m de rações!'.format(largura, altura, unirac))
print('')
print('\033[36;40mFoi um enorme prazer te ajudar, senhor {}!\033[m'.format(nome))
