#

midd = hom = mul = 0

print('--' * 10)
print('CADASTRE UMA PESSOA')
print('--' * 10)

while True:

    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    while not sexo in 'MF':
        sexo = str(input('Valor Invalido.\n'
                         'Informe Sexo [M/F]:')).strip().upper()[0]
    if idade >= 18:
        midd += 1
    if sexo == 'M':
            hom += 1
    if sexo == 'F' and idade < 20:
        mul += 1

    continuar = str(input('Quer Continuar? [S/N]: ')).strip().upper()[0]

    while not continuar in 'SN':
        continuar = str(input('Valor Invalido.\n'
                              'Quer Continuar? [S/N: ')).strip().upper()[0]
    print('--' * 10)
    if continuar == 'N':
        break

print(f'Foram Cadastradas {midd} Pessoas Maior de 18 Anos.')
print(f'Foram Cadastrados {hom} Homens.')
print(f'Foram Cadastradas {mul} Mulheres Menores de 20 Anos.')
