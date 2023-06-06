# Progressão Aritmética 2.

print('-=' * 10)
print('10 Termos de uma PA')
print('-=' * 10)

cont = 1
total = 10
continuar = 1
pt = int(input('Digite o 1º Termo: '))
rz = int(input('Digite altura Razão: '))

while continuar != 0:
    while cont <= total:
        print(pt, end=' -> ')
        pt += rz
        cont += 1

    continuar = int(input('Pausa.\n'
                          'Você quer mostrar mais quantos termos? '))
    total += continuar

print(f'Progressão Finalizada. {total} Mostrados.')
