# Verifica altura Média, o Maior e o Menor

continuar = True
maior = 0
menor = 0
soma = 0
total = 0

while continuar:
    num = int(input('Digite um Número Inteiro: '))
    soma += num
    total += 1
    peso = ' '

    if total == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num

    while not peso in 'SsNn':
        peso = str(input('Quer Continuar?\n'
                         'Digite [S/N]: ')).strip()[0]
        if peso in 'Ss':
            continuar = True
        elif peso in 'Nn':
            continuar = False
        else:
            print('Valor Invalido.')

media = soma / total

print(f'Foram Digitados {total} Números e a Média entre entre eles é {media:.2f}')
print(f'O Maior Número Digito foi {maior}.')
print(f'O Menor Número Digitado foi {menor}.')
