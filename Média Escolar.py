professor = str(input('Por favor, insira o seu nome: '))
print('Seja bem-vindo Professor(a) {}!'.format(professor))
escola = str(input('Como é o nome da escola que deseja consultar? '))
aluno = str(input('E o nome do aluno em específico? '))
turma = str(input('E de qual turma ele é? '))
nota1 = float(input('Qual a primeira nota do aluno {}? '.format(aluno)))
nota2 = float(input('Qual a segunda nota do aluno {}? '.format(aluno)))
nota3 = float(input('Qual a terceira nota do aluno {}? '.format(aluno)))
nota4 = float(input('Qual a quarta nota do aluno {}? '.format(aluno)))
nota5 = float(input('Qual a quinta nota do aluno {}? '.format(aluno)))
soma = nota1 + nota2 + nota3 + nota4 + nota5
media = soma / 5
print('O aluno {}, da turma {}, da escola {}, teve uma média nas notas de: {:.1f}!'.format(aluno, turma, escola, media))
