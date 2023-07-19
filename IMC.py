print('OlÁ, seja bem-vindo(a)!'.upper())
print('')
nome = str(input('Por favor, diga o seu nome: ')).strip()
peso = float(input('Por favor, digite o seu peso: KG'))
altura = float(input('Por favor, digite a sua altura: M'))
print('')
print('O seu nome é: {}. \n o seu peso é: {:.0f}kg. \n a sua altura é: {:.2f}m.'.format(nome, peso, altura))
print('')
IMC = peso / (altura ** 2)
# print(IMC)
if IMC < 18.5:
    print('Você está abaixo do peso ideal. Seu Índice de Massa Corporal é {:.1f}'.format(IMC))
elif IMC > 18.5 and IMC < 25:
    print('Você está no peso ideal. Seu Índice de Massa Corporal é {:.1f}'.format(IMC))
elif IMC > 25 and IMC < 30:
    print('Você está acima do peso ideal. Seu Índice de Massa Corporal é {:.1f}'.format(IMC))
elif IMC > 30 and IMC < 40:
    print('Você está com Obesidade. Seu Índice de Massa Corporal é {:.1f}'.format(IMC))
elif IMC > 40:
    print('Você está com Obesidade Mórbida. Seu Índice de Massa Corporal é {:.1f}'.format(IMC))
print('')
print('Foi um prazer lhe ajudar a descobrir o seu IMC!'.upper())
