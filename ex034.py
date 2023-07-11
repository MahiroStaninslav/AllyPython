nomef = str(input('Como é o nome do Funcionário? ')).strip()
salario = float(input('Quanto é o salário do funcionário {}? R$'.format(nomef)))
aumento1 = (salario * 10) / 100
aumento2 = (salario * 15) / 100
if salario > 1250:
    print('O salário do funcionário {}, com o aumento de 10%, ficará R${:.2f}'.format(nomef, aumento1 + salario))
else:
    print('O salário do funcionário {}, com o aumento de 15%, ficará R${:.2f}'.format(nomef, aumento2 + salario))
