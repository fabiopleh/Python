# Verifica altura Maioridade.

from datetime import date

nasc = 0
maior = 0
menor = 0

for c in range(1, 8):
    nasc = int(input(f'Digite o {c}º Ano do seu Nascimento: '))
    idade = date.today().year - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print(f'{maior} Pessoas São Maiores de Idade.')
print(f'{menor} Pessoas São Menores de Idade.')
