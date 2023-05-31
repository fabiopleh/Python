# Acerte o Número.
from random import randint
x = randint(0, 5)
print('-=-' * 23)
print('Vou pensar em um Número entre 0 e 5. Tente Adivinhar...')
print('-=-' * 23)
y = int(input('Em que Número eu Pensei? '))

if y == x:
    print('PARABÉNS!! Você Ganhou!')
else:
    print(f'GANHEI!! Eu pensei no Número {x} e não no {y}.')
