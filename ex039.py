from datetime import date
from time import sleep
#nome = str(input('Olá, como é o seu nome? ')).strip()
#nascimento = int(input('Quantos anos você tem? '))
#if nascimento == 18:
#    print('Você está na idade certa para se alistar no serviço militar.')
#elif nascimento < 18:
#    print('Você ainda está muito novo para se alistar e faltam {} anos.'.format(18 - nascimento))
#elif nascimento > 18:
#    print('Você passou da hora de se alistar no serviço militar e está {} anos atrasado!'.format(nascimento - 18))

print('Seja bem-vindo ao calculador de alistamento!'.upper())
sleep(1)
AnoAtual = date.today().year
nascimento = int(input('Em qual ano você nasceu? '))
print('')
print('Quem nasceu em {}, tem {} anos em {}!'.format(nascimento, AnoAtual - nascimento, AnoAtual))
print('')
sexo = str(input('Você é do sexo Masculino ou Feminino? ').lower()).strip()
print('')
idade = AnoAtual - nascimento
if sexo == 'feminino':
    print('Você pode se alistar, mas não é obrigatório.')
    print('')
    if idade == 18:
        print('Você está na idade certa, e deve se alistar este ano, {}.'.format(AnoAtual))
    elif idade > 18:
        print('você já passou da hora de se alistar, está {} anos atrasado e deveria ter se alistado em {}!'.format(idade - 18, AnoAtual - (idade - 18)))
    elif idade < 18:
        print('Você ainda está muito novo para se alistar, ainda faltam {} anos e vai se alistar em {}!'.format(18 - idade, AnoAtual + (18 - idade)))
