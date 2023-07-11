from random import shuffle, sample
prof = str(input('Olá! Como é o seu nome, professor(a)? '))
alun = str(input('Qual o nome do primeiro aluno? '))
alun2 = str(input('E do segundo aluno? '))
alun3 = str(input('E do terceiro aluno? '))
alun4 = str(input('E do quarto aluno? '))
aluns = [alun, alun2, alun3, alun4]
sortear = sample(aluns, k=4)
print('Professor {}, esta será a ordem dos alunos que apresentarão primeiro até o último da lista; {}!'.format(prof, sortear))

student1 = str(input('What is the name of the first student? '))
student2 = str(input('What is the name of the second student? '))
student3 = str(input('What is the name of the third student? '))
student4 = str(input('What is the name of the fourth student? '))
students = [student1, student2, student3, student4]
shuffle(students)
print('The students selected for the presentation, will be in this order: {}'.format(students))
