# Seno, Cosseno e Tangente.

from math import radians, sin, cos, tan

ang = float(input('Digite o ângulo desajado: '))
sen = sin(radians(ang))
print(f'O Ângulo {ang} tem o Seno de {sen:.2f}.')
cos = cos(radians(ang))
print(f'O Ângulo {ang} tem o Cosseno de {cos:.2f}.')
tg = tan(radians(ang))
print(f'O Ângulo {ang} tem a Tangente de {tg:.2f}.')
