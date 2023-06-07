# Jogo PAR ou ÍMPAR.

from random import randint
total = 0
rdd = 1

print('~~' * 13)
print('Vamos Jogar PAR ou ÍMPAR!')
print('~~' * 13)

while True:

    jogador = int(input('Digite um Valor: '))
    pi = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    pc = randint(1, 10)
    soma = pc + jogador
    print('--' * 13)

    while not pi in 'PpIi':
        pi = str(input('Valor Invalido,\n'
                       'Par ou Ímpar [P/I]: ')).strip().upper()[0]

    print(f'Você jogou {jogador} e o Computador {pc}. O total é {soma}.')
    print('Deu PAR.' if soma % 2 == 0 else 'Deu ÍMPAR.')

    if soma % 2 == 0:
        if pi in 'P':
            print('Você VENCEU!!!')
        else:
            break

    if soma % 2 != 0:
        if pi in 'I':
            print('Você VENCEU!!!')
        else:
            break
    print('Vamos Continuar...')
    total += 1
    print('--' * 13)

print('Você PERDEU!')
print(f'Fim do Jogo. Você Venceu {total} vezes.')
