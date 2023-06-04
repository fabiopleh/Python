# Criando Menu de Opções.

from time import sleep
num1 = int(input('Digite o 1º Número: '))
num2 = int(input('Digite o 2º Número: '))
menu = 0

while menu != 5:
    print('-=' * 13)
    menu = int(input('[ 1 ] Somar\n'
                     '[ 2 ] Multiplicar\n'
                     '[ 3 ] Maior\n'
                     '[ 4 ] Novos Números\n'
                     '[ 5 ] Sair do Programa\n'
                     'Escolha uma Opção: '))
    print('-=' * 13)

    if menu == 1:
        print(f'A Soma Entre {num1} e {num2} é {num1 + num2}')
    elif menu == 2:
        print(f'A Multiplicação Entre {num1} e {num2} e {num1 * num2}')
    elif menu == 3:
        if num1 > num2:
            print(f'O Maior Número Entre {num1} e {num2} é {num1}')
        else:
            print(f'O Maior Número Entre {num1} e {num2} é {num2}')
    elif menu == 4:
        print('Digite Novos Números')
        num1 = int(input('Digite o 1º Número: '))
        num2 = int(input('Digite o 2º Número: '))
    elif menu == 5:
        print('Finalizando...')
    else:
        print('Opção Invalida. Tente Novamente.')
    sleep(1.5)

print("Fim do Programa.")
