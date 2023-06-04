# Verifica o Maior e o Menor Peso.

maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input(f'Digite o Peso da {c} Pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O Maior Peso foi {maior}')
print(f'O Menor Peo foi {menor}')
