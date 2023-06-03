# Soma Números Pares.

num = 0
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º Número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você Digitou {cont} Números Pares e a Soma é {soma}.')
