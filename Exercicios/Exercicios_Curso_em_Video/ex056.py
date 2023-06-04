# Analisando Dados.

media = 0
homem = 0
mulher = 0
nomeh = ''

for c in range(1, 5):
    print(f'----- {c}º PESSOA -----')
    nome = str(input(f'Nome: ')).strip().capitalize()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo [M/F] : ')).strip()

    media += idade

    if sexo in 'Mm' and idade > homem:
        homem = idade
        nomeh = nome

    if sexo in 'Ff' and idade < 20:
        mulher += 1

print(f'A Média de Idade do Grupo é {media / c:.1f}.')
print(f'O Nome Do Homem Mais Velho é {nomeh} e ele tem {homem} Anos.')
print(f'A Quantidade de Mulheres com Menos de 20 Anos é {mulher}.')
