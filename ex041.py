from time import localtime
atleta = str(input('Como é o nome do atleta? ')).strip()
nascimento = int(input('Qual o ano de nascimento do atleta {}? '.format(atleta)))
tempo = localtime().tm_year
restrição = tempo - nascimento
if restrição <= 9:
    print('mirim'.upper())
elif restrição > 9 and restrição <= 14:
    print('infantil'.upper())
elif restrição > 14 and restrição <= 19:
    print('junior'.upper())
else:
    print('Master'.upper())
print('Pois o {} tem {} anos.'.format(atleta, restrição))
