# Conversor de Bases Numéricas.

num = int(input('Digite um Número Inteiro: '))
print('Para a Base de Conversão:\n'
      '[ 1 ] - Binário\n'
      '[ 2 ] - Octual\n'
      '[ 3 ] - Hexadecimal')

op = int(input('Digite sua Opção: '))

if op == 1:
    print(f'{num} Convertido para Binário é {bin(num)[2:]}')
elif op == 2:
    print(f'{num} Convertido para Octual é {oct(num)[2:]}')
elif op == 3:
    print(f'{num} Convertido para Hexadecimal é {hex(num)[2:]}')
else:
    print('Opção Inválida.')
    