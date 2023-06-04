# Sorteando uma Ordem na lista.

from random import shuffle

al1 = input('Primeiro Aluno: ')
al2 = input('Segundo Aluno: ')
al3 = input('Terceiro Aluno: ')
al4 = input('Quarto Aluno: ')

la = [al1, al2, al3, al4]
shuffle(la)

print('A Ordem do Sorteio dos Alunos é:')

for al in la:
    print(al)
