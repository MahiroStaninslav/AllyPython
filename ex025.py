name = str(input('Digite um nome completo: ')).strip()
print('Analisando o nome "{}" ...'.format(name))
print('No nome escrito tem Silva: {}'.format('Silva'.title() in name))
print('Seu nome tem {} Letras!'.format(len(name) - name.count(' ')))
