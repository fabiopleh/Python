# Calculando Fatorial (Com Laço 'for').

num = int(input('Calculando Fatorial.\n'
                'Digite um Número: '))
res = num

print(f'Calculando {num}! = ', end='')

for c in range(num, 0, -1):
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    if c < num:
        res *= c

print(res)
