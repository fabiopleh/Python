# Verifica se é um Palíndromo.

frase = str(input('Digite uma Frase: ')).lower()
frase = frase.split()
frase = ''.join(frase)
# frase_inv = frase[::-1]
frase_inv = ''

for letra in range(len(frase) - 1, -1, -1):
    frase_inv += frase[letra]

print(f'O Inverso de {frase} é {frase_inv}.')

if frase == frase_inv:
    print('Essa Frase é um Palíndromo.')
else:
    print('Essa Frase não é um Palíndromo.')
