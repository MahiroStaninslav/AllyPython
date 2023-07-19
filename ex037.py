num = int(input('Olá usuário! Tudo Bem? Digite um número inteiro de sua escolha: '))
print('')
base = int(input('Agora, você vai escolher uma base de conversão; \n digite [ 1 ] para binário,'
                 ' \n digite [ 2 ] para octal, \n digite [ 3 ] para hexadecimal: '))
if base == 1:
    print('O resultado para a base de conversão binário será: {}'.format(bin(num)[2:]))
elif base == 2:
    print('O resultado para a base de conversão octagonal será: {}'.format(oct(num)[2:]))
elif base == 3:
    print('O resultado para a base de conversão hexagonal será: {}'.format(hex(num)[2:]))
else:
    print('Você não digitou a \033[31mnumeração correta\033[31m.')
