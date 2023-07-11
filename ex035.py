comp1 = int(input('Qual o primeiro comprimento? '))
comp2 = int(input('Qual o segundo comprimento? '))
comp3 = int(input('Qual o terceiro comprimento? '))
A = comp2 + comp3
B = comp1 + comp3
C = comp1 + comp2
if A > comp1:
    if B > comp2:
        if C > comp3:
            print('É possível formar um triângulo, pois a soma dos dois lados é maior que o maior comprimento!')
else:
    print('Não é possível formar um triângulo, pois a soma dos dois lados é menor do que o valor absoluto!')
