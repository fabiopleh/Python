# Calcula o IMC.

peso = float(input('Informe seu Peso: '))
altura = float(input('Informe sua Altura: '))
imc = peso / (altura ** 2)

print(f'O IMC é de {imc:.1f}')

if imc < 18.5:
    print('Abaixo do Peso')
elif 18.5 <= imc < 25:
    print('Peso Ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
