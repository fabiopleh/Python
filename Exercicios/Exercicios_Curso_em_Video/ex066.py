# Vários Números com Flag.

total = soma = 0

while True:
    num = int(input('Digite um Número[999 para Parar]: '))
    if num == 999:
        break
    total += 1
    soma += num

print(f'A Soma dos {total} Números é {soma}.')
