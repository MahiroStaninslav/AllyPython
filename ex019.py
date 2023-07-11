from random import choice
prof = str(input('Olá! Como é o seu nome, professor(a)? '))
alun = str(input('Qual o nome do primeiro aluno? '))
alun2 = str(input('E do segundo aluno? '))
alun3 = str(input('E do terceiro aluno? '))
alun4 = str(input('E do quarto aluno? '))
aluns = [alun, alun2, alun3, alun4]
sortear = choice(aluns)
print('Professor {}, o aluno sorteado para apagar o quadro foi {}!'.format(prof, sortear))
