import math
from math import sin, cos, tan, pi, radians

'''angulo = float(input('Escolha um ângulo qualquer: º'))

xrad1 = pi / 2  # ângulo de 90 graus.

xrad2 = pi / 3  # ângulo de 60 graus.

xrad3 = pi / 4  # ângulo de 45 graus.

xrad4 = pi / 6  # ângulo de 30 graus.

xrad5 = 2 * pi  # ângulo de 360 graus.

xrad6 = 11 * pi / 6  # ângulo de 330 graus.

xrad7 = 7 * pi / 4  # ângulo de 315 graus.

xrad8 = 5 * pi / 3  # ângulo de 300 graus.

xrad9 = 3 * pi / 2  # ângulo de 270 graus.

xrad10 = 4 * pi / 3  # ângulo de 240 graus.

xrad11 = 5 * pi / 4  # ângulo de 225 graus.

xrad12 = 7 * pi / 6  # ângulo de 210 graus.

xrad13 = pi  # ângulo de 180 graus.

xrad14 = 5 * pi / 6  # ângulo de 150 graus.

xrad15 = 3 * pi / 4  # ângulo de 135 graus.

xrad16 = 2 * pi / 3  # ângulo de 120 graus.

radconversor = radians(angulo)

if angulo == 90:
    sen = sin(xrad1)
    cos = cos(xrad1)
    tan = tan(xrad1)
if angulo == 60:
    sen = sin(xrad2)
    cos = cos(xrad2)
    tan = tan(xrad2)
if angulo == 45:
    sen = sin(xrad3)
    cos = cos(xrad3)
    tan = tan(xrad3)
if angulo == 30:
    sen = sin(xrad4)
    cos = cos(xrad4)
    tan = tan(xrad4)
if angulo == 360:
    sen = sin(xrad5)
    cos = cos(xrad5)
    tan = tan(xrad5)
if angulo == 330:
    sen = sin(xrad6)
    cos = cos(xrad6)
    tan = tan(xrad6)
if angulo == 315:
    sen = sin(xrad7)
    cos = cos(xrad7)
    tan = tan(xrad7)
if angulo == 300:
    sen = sin(xrad8)
    cos = cos(xrad8)
    tan = tan(xrad8)
if angulo == 270:
    sen = sin(xrad9)
    cos = cos(xrad9)
    tan = tan(xrad9)
if angulo == 240:
    sen = sin(xrad10)
    cos = cos(xrad10)
    tan = tan(xrad10)
if angulo == 225:
    sen = sin(xrad11)
    cos = cos(xrad11)
    tan = tan(xrad11)
if angulo == 210:
    sen = sin(xrad12)
    cos = cos(xrad12)
    tan = tan(xrad12)
if angulo == 180:
    sen = sin(xrad13)
    cos = cos(xrad13)
    tan = tan(xrad13)
if angulo == 150:
    sen = sin(xrad14)
    cos = cos(xrad14)
    tan = tan(xrad14)
if angulo == 135:
    sen = sin(xrad15)
    cos = cos(xrad15)
    tan = tan(xrad15)
if angulo == 120:
    sen = sin(xrad16)
    cos = cos(xrad16)
    tan = tan(xrad16)

# noinspection PyUnboundLocalVariable
print('O Seno do Ângulo {:.0f}º, é {:.2f}!'.format(angulo, sen))
print('O Cosseno do Ângulo {:.0f}º, é {:.2f}!'.format(angulo, cos))
print('O Tangente do Ângulo {:.0f}º, é {:.2f}!'.format(angulo, tan))'''

ângulo = int(input('Digite um ângulo: '))
seno = math.sin(math.radians(ângulo))
print('O Seno do ângulo {} é {:.2f} !'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O Cosseno do ângulo {} é {:.2f} !'.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('O Tangente do ângulo {} é {:.2f} !'.format(ângulo, tangente))
