# Verifica se as Retas Formam um Triângulo e o Classifica.

r1 = int(input('Primeiro Seguimento: '))
r2 = int(input('Segundo Seguimento: '))
r3 = int(input('Terceiro Seguimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas Retas Podem Formar um Triângulo ', end='')
    if r1 == r2 == r3:
        print('Equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('Essas Retas não formam um Triângulo')
