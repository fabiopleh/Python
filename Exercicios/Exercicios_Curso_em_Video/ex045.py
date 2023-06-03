#PEDRA PAPEL TESOURA

from random import randint
itens = ('', 'Pedra', 'Papel', 'Tesoura')
pc = randint(1, 3)
print('Vamos Jogar PEDRA, PAPEL, TESOURA!')
us = int(input('[ 1 ] Pedra\n'
               '[ 2 ] Papel\n'
               '[ 3 ] Tesoura\n'
               'Escolha sua Jogada: '))
print('-=' * 15)
print(f'O Computador Escolheu {itens[pc]}')
print(f'Você Escolheu {itens[us]}')
print('-=' * 15)
if pc == 1:
    if us == 1:
        print('Empate')
    elif us == 2:
        print('PARABÊNS! Você Venceu!')
    elif us == 3:
        print('Você Perdeu.')
    else:
        print('Opção Invalida.')
if pc == 2:
    if us == 2:
        print('Empate')
    elif us == 3:
        print('PARABÊNS! Você Venceu!')
    elif us == 1:
        print('Você Perdeu.')
    else:
        print('Opção Invalida.')
if pc == 3:
    if us == 3:
        print('Empate')
    elif us == 1:
        print('PARABÊNS! Você Venceu!')
    elif us == 2:
        print('Você Perdeu.')
    else:
        print('Opção Invalida.')
