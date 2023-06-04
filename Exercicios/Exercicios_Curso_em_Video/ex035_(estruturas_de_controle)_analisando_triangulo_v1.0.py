# Analisando Triângulo v1.0.

seg1 = float(input('Digite o 1° Seguimento: '))
seg2 = float(input('Digite o 2° Seguimento: '))
seg3 = float(input('Digite o 3° Seguimento: '))

if seg1 + seg2 > seg3 and seg1 + seg3 > seg2 and seg2 + seg3 > seg1:
    print('Essas Retas Podem Formar um Triângulo.')
else:
    print('Essas Retas não Formam um Triângulo.')
