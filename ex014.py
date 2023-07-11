temp = int(input('Informe a temperatura em C°: C°'))
# 'temperatura de Celsius para Kelvin é é "Temperatura Kelvin = Temperatura Celsius + 273", então TK = resultado.'
tempK = temp + 273
# 'temperatura de Celsius para Fahrenheit é "Temperatura Celsius/5 = (Temperatura Fahrenheit – 32)/9
# OU Fahrenheit = ((9 * Celsius) / 5) + 32".'
tempF1 = temp * 9 + 160
tempF2 = tempF1 / 5
print('Sua temperatura Graus Celsius em Cº{} para Kelvin ficá Kº{} e em Fahrenheit fica Fº{}.'.format(temp, tempK, tempF2))
