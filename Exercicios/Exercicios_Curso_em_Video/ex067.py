#

while True:

    num = int(input('Digite um Valor Para ver altura Sua Tabuada: '))

    print('-=' * 6)

    if num <= 0:
        break

    for cont in range(1, 11):
        print(f'{num} x {cont:2} = {num * cont}')

    print('-=' * 6)

print('Programa Finalizado.')
