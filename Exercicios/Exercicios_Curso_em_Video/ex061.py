# Progressão Aritmética 2.

print('-=' * 10)
print('10 Termos de uma PA')
print('-=' * 10)

pt = int(input('Digite o 1º Termo: '))
rz = int(input('Digite altura Razão: '))
cn = 10

while cn > 0:
    print(pt, end=' -> ')
    pt += rz
    cn -= 1

print('FIM!')
