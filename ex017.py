from math import hypot
nome = str(input('Como é o seu nome? '))
catopos = float(input('Bem-vindo(a) {}, qual o comprimento do cateto oposto? '.format(nome)))
catadja = float(input('E o comprimento do cateto adjacente? '))
hipotenusa = hypot(catopos, catadja)
print('O comprimento da hipotenusa é de: {:.2f}'.format(hipotenusa))
print('')
hi = (catopos ** 2 + catadja ** 2) ** (1/2)
print(hi)
