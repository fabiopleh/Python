# Adivinhando Número.

from random import randint

print('Vou Pensar em Número Entre 1 e 10. Tente Adivinha.')
pc = randint(1, 10)
us = int(input('Qual é Seu Palpite: '))
ten = 1

while not us == pc:
    if pc > us:
        print(f'É um Número Maior.', end=' ')
    else:
        print(f'É um Número menor.', end=' ')
    print('Tente Novamente.')
    us = int(input('Qual é Seu Palpite: '))
    ten += 1

print(f'PARABÉNS!!! Você Acertou com {ten} Tentativa!')
