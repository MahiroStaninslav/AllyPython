nome = str(input('Como é o nome do funcionário? '))
salario = float(input('Quanto é o Salário do funcionário {}? R$'.format(nome)))
aumento = salario + (salario * 15 / 100)
print('O salário R${:.2f} do funcionário {} com o aumento de 15%, ficará R${:.2f}!'.format(salario, nome, aumento))
