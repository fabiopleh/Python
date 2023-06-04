# Progressão Aritmética.

print('=' * 20)
print('10 Termos de uma PA')
print('=' * 20)

pt = int(input('Digite o 1º Termo: '))
r = int(input('Digite altura Razão: '))
dc = pt + (10 - 1) * r

for c in range(pt, dc + r, r):
    print(c, end=' -> ')
print('FIM!')
