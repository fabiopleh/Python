# Calcula Impares Multiplos de 3 até 500.

soma = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'São {cont} Valores que Somados Resulta {soma}')
