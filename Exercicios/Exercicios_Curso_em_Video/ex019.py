# Sorteando um Item na Lista.

from random import choice

al1 = input('Primeiro Aluno: ')
al2 = input('Segundo Aluno: ')
al3 = input('Terceiro Aluno: ')
al4 = input('Quarto Aluno: ')
la = choice([al1, al2, al3, al4])

print(f'O Aluno Escolhido foi {la}.')
