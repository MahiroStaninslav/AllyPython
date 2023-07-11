nome = str(input('Seja bem-vindo ao código do Lorde Maho. Como o Senhor(a) se chama? '))

numero = int(input('Muito bem Mestre {}, qual número você deseja? '.format(nome)))
print('O seu Número Escolhido é: {}, seu Antecessor é: {}, e o seu Sucessor é: {}!'.format(numero, numero-1, numero+1))

algoritmo = int(input('E qual o próximo número desejas, {}? '.format(nome)))
print('O seu Número é: {}, o seu Dobro é: {}, o seu Triplo é: {} ... '
      ' \n por fim, sua Raiz Quadrada é: {:.1f}!'.format(algoritmo, algoritmo*2, algoritmo*3, algoritmo**(1/2)))
print('Foi um prazer poder te ajudar, mestre {}!'.format(nome))
