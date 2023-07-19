from time import sleep
cores = {'red': '\033[31m', 'yellow': '\033[33m', 'blue': '\033[34m', 'cyano': '\033[36;40m', 'clear': '\033[m'}

print('Olá, seja bem-vindo!'.upper())

sleep(1)

print('')

comp1 = int(input('Qual o Primeiro comprimento? '))

print('')

comp2 = int(input('Qual o Segundo comprimento? '))

print('')

comp3 = int(input('Qual o Terceiro comprimento? '))

print('')
A = comp2 + comp3
B = comp1 + comp3
C = comp1 + comp2
if A > comp1 or B > comp2 or C > comp3:
    print('É possível formar um triângulo, pois a {}soma dos dois lados é maior que o valor absoluto{}!'.format(cores['cyano'], cores['clear']))
    print('')
    if comp1 == comp2 or comp1 == comp3 or comp2 == comp3:
        print('Este triângulo é um {}Isósceles{}, pois ele possuí {}dois lados iguais{}!'.format(cores['yellow'], cores['clear'], cores['cyano'], cores['clear']))
        print('')
    elif comp1 != comp2 and comp1 != comp3 and comp2 != comp3:
        print('Este triângulo é um {}Escaleno{}, pois ele possuí {}todos os lados diferentes{}!'.format(cores['red'], cores['clear'], cores['cyano'], cores['clear']))
        print('')
else:
    print('Não é possível formar um triângulo, pois a soma de dois lados \033[31mé menor do que o valor absoluto\033[m!')
    if comp1 == comp2 and comp1 == comp3 and comp2 == comp3:
        print('Este triângulo é um {}Equilátero{}, pois {}todos os lados são iguais{}!'.format(cores['blue'], cores['clear'], cores['cyano'], cores['clear']))
