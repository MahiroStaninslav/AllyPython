nome = str(input('Como é o seu nome completo? ')).strip()
nome = (nome.split())
print('Olá, seja bem-vindo! \n Primeiro Nome: {} \n Sobrenome: {} '
      '\n Último Nome: {}'.format(nome[0], nome[len(nome)-1], nome[1]))
