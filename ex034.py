# On that line, I asked the name of the employer, using the "strip" function to remove all unnecessary spaces.
# Then, I asked the salary of the worker, and created two variables, one with 10% increase, and the other with 15%.
nomef = str(input('Como é o nome do Funcionário? ')).strip()

salario = float(input('Quanto é o salário do funcionário {}? R$'.format(nomef)))

aumento1 = (salario * 10) / 100
aumento2 = (salario * 15) / 100

# Here I have used the "If" condition, so if the salary is higher than R$1250, it will print it, colorize the 10% ...
# and then say how much he will receive in the end! Otherwise, it will increase only 15%.
if salario > 1250:
    print('O salário do funcionário {}, com o '
          '\033[1;33maumento de 10%\033[m, ficará R${:.2f}'.format(nomef, aumento1 + salario))
else:
    print('O salário do funcionário {}, com o '
          '\033[1;32maumento de 15%\033[m, ficará R${:.2f}'.format(nomef, aumento2 + salario))
