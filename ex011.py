welcome = str(input('Seja bem-vindo(a)! Como o Senhor ou Senhora se chama? '))
print('Seja bem-vindo Pintor {}!'.format(welcome))
larg = float(input('Qual a largura da parede em Metros? '))
altu = float(input('E a altura? '))
area = larg * altu
print('Sua parede tem {}x{}, e sua área mede {}m².'.format(larg, altu, area))
tinp = area / 2
print('Para pintar esta parede, você vai precisar de {} litros de tinta.'.format(tinp))
