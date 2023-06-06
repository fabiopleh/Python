# Tratando Vários Valores v1.0.

num = 0
total = 0
soma = 0

while not num == 999:
    num = int(input('Digite um Número [999 para Parar]: '))
    if num != 999:
        total += 1
        soma += num

print(f'O total de Números digitados foi {total} e a soma entre eles é {soma}.')
