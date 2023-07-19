'''numero1 = int(input('Escolha o primeiro número: '))
numero2 = int(input('Escolha o segundo número: '))
if numero1 > numero2:
    print('O número {} é maior que o número {}!'.format(numero1, numero2))
else:
    print('O número {} é menor que o número {}!'.format(numero1, numero2))'''

a = int(input('Escolha um número: '))
b = int(input('Escolha um número: '))
c = int(input('Escolha um numero: '))
# Verificando qual é o menor número dentre os três.
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor número dentre os três números, é o {}!'.format(menor))
# Verificando qual é o maior número dentre os três.
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior número dentre os três números, é o {}!'.format(maior))
