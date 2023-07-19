# Here, I have created a program that will tell you if you could actually form a TRIANGLE with the 3 lens.
# To do that, you firstly get the highest number as the base, then, if the sum of the smaller numbers ...
# result in getting bigger than the first number, it will form a triangle and tell you why it formed it! ...
# Otherwise, it will say why it is not possible to form a triangle.
comp1 = int(input('Qual o primeiro comprimento? '))

comp2 = int(input('Qual o segundo comprimento? '))

comp3 = int(input('Qual o terceiro comprimento? '))

A = comp2 + comp3
B = comp1 + comp3
C = comp1 + comp2

if A > comp1:
    if B > comp2:
        if C > comp3:
            print('\033[4;32mÉ possível\033[m formar um triângulo, pois a '
                  '\033[32msoma dos dois lados é maior\033[m que o maior comprimento!')
else:
    print('\033[4;31mNão é possível\033[m formar um triângulo, pois a '
          '\033[31msoma dos dois lados é menor\033[m do que o valor absoluto!')
