aluno = str(input('Como é o nome do aluno? ')).strip()
nota1 = float(input('Qual é a primeira nota do aluno? '))
nota2 = float(input('Qual é a segunda nota do aluno? '))
média = (nota1 + nota2) / 2
if média < 5.0:
    print('O aluno {} foi \033[31mREPROVADO\033[m!'.format(aluno))
if média > 5.0 and média < 6.9:
    print('O aluno {} ficou de \033[33mRECUPERAÇÃO\033[m!'.format(aluno))
if média >= 7.0:
    print('O aluno {} foi \033[32mAPROVADO\033[m!'.format(aluno))
print('Sua média de notas foi de {}!'.format(média))
