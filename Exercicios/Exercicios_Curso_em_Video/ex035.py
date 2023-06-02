# Analisa se Três Retas Podem Formam um Triângulo.
r1 = float(input('Digite o Valor da 1° Reta: '))
r2 = float(input('Digite o Valor da 2° Reta: '))
r3 = float(input('Digite o Valor da 3° Reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Essas Retas Podem Formar um Triângulo.')
else:
    print('Essas Retas não Formam um Triângulo.')
