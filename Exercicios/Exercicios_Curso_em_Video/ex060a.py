# Calculando Fatorial (Com Laço 'while').

num = int(input('Calculando Fatorial.\n'
                'Digite um Número: '))
con = num
res = 1

print(f'Calculando {num}!', end=' = ')

while con > 0:
    print(con, end='')
    print(' x ' if con > 1 else ' = ', end='')
    res *= con
    con -= 1

print(res)
