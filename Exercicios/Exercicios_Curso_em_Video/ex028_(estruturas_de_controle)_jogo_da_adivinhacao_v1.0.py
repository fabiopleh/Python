# Jogo da Adivinhação v1.0.

from random import randint

numpc = randint(1, 5)
print('-=-' * 20)
print(f'{"Vou pensar em um Número entre 1 e 5. Tente Adivinhar...":^60}')
print('-=-' * 20)
numuser = int(input('Em que Número eu Pensei? '))

if numuser == numpc:
    print('PARABÉNS!! Você Ganhou!')
else:
    print(f'GANHEI!! Eu pensei no Número {numpc} e não no {numuser}.')
