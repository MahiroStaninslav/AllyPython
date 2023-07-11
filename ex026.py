frase = str(input('Digite uma frase aí: ')).strip()
print('Em sua frase, a letra "a" aparece {} vezes.'.format(frase.lower().count('a')))
print('Em sua frase, a letra "a" aparece pela primeira vez'
      ' no índice {} e na posição {}.'.format(frase.lower().find('a'), frase.lower().find('a')+1))
print('Em sua frase, a letra "a" aparece pela última vez'
      ' no índice {} e na posição {}.'.format(frase.lower().rfind('a'), frase.lower().rfind('a')+1))
