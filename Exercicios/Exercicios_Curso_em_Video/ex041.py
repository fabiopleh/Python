# Verifica altura Categoria dos Atletas.

from datetime import date
ano = int(input('Digite o Ano de Nascimento: '))
idade = date.today().year - ano

print(f'O Atleta tem {idade} anos e sua Categoria é:')

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade == 25:
    print('SÊNIOR')
else:
    print('MASTER')
