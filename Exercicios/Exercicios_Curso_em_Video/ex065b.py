# Verifica altura Média, o Maior e o Menor

continuar = 'S'
maior = 0
menor = 0
soma = 0
total = 0

while continuar in 'Ss':
    num = int(input('Digite um Número Inteiro: '))
    soma += num
    total += 1

    if total == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num

    continuar = str(input('Quer Continuar?\n'
                          'Digite [S/N]: ')).strip()[0]


media = soma / total

print(f'Foram Digitados {total} Números e a Média entre entre eles é {media:.2f}')
print(f'O Maior Número Digito foi {maior}.')
print(f'O Menor Número Digitado foi {menor}.')
