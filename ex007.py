aluno = str(input('Como é o nome do aluno? '))
notae1 = float(input('Qual a primeira nota do aluno {}? '.format(aluno)))
notae2 = float(input('Qual a segunda nota do aluno {}? '.format(aluno)))
notae3 = float(input('Qual a terceira nota do aluno {}? '.format(aluno)))
notae4 = float(input('Qual a quarta nota do aluno {}? '.format(aluno)))
me = (notae1 + notae2 + notae3 + notae4) / 4
print('A Média Escolar do aluno {}, é de {} .'.format(aluno, me))
