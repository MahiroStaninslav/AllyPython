nome = input('O que você quer escrever? \033[31m')
print('O tipo primitivo do que você escreveu é:', type(nome))
print(f'"{nome}\033[m" é Alfabético? ', nome.isalpha())
print(f'"{nome}\033[m" é um Número? ', nome.isnumeric())
print(f'"{nome}\033[m" é Alfanumérico? ', nome.isalnum())
print(f'"{nome}\033[m" está capitalizada? ', nome.istitle())
print(f'"{nome}\033[m" está em MAIÚSCULO? ', nome.isupper())
print(f'"{nome}\033[m" está em minúsculo? ', nome.islower())
print('"\033[33m{}\033[m" é Assimétrico? '.format(nome), nome.isascii())
numero1 = int(input('Escolha um número e em seguida o próximo: '))
numero2 = int(input('E o outro número? '))
resultado = numero1+numero2
resultado2 = numero1-numero2
resultado3 = numero1*numero2
resultado4 = numero1/numero2
print('O resultado da operação em soma é de "{}" '.format(resultado), 'e seu tipo primitivo é ', type(resultado))
print('O resultado da operação em subtração é de "{}"'.format(resultado2), 'e seu tipo primitivo é ', type(resultado2))
print('O resultado da operação em multiplicação é de "{}"'.format(resultado3), 'e seu tipo primitivo é ', type(resultado3))
print('O resultado da operação em divisão é de "{}"'.format(resultado4), 'e seu tipo primitivo é ', type(resultado4))
