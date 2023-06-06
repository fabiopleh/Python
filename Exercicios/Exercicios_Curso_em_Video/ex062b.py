# Prpgressão Aritimetica 3.

cont = 10
continuar = 0
parar = False
total = 0
pt = int(input('Digite o 1º Termo: '))
rz = int(input('Digite altura Razão: '))

while not parar:
    if cont > 0:
        print(pt, end=' -> ')
        pt += rz
        cont -= 1
        total += 1
    elif cont == 0:
        continuar = int(input('Pausa\n'
                              'Você quer Mostras mais Quantos Termos: '))
        if continuar > 0:
            cont += continuar
        else:
            parar = True

print(f'Progressão Finalizada. {total} Mostrados.')
