# Catetos e Hipotenusa.

from math import hypot

co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))

hi = hypot(co, ca)
# hi = (co ** 2 + ca ** 2) ** (1/2)

print(f'A Medida da Hipotenusa é {hi:.2f}.')
