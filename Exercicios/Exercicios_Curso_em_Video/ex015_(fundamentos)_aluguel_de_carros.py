# Aluguel de Carros.

diaria = int(input('Quantos Dias Alugados: '))
km = float(input('Quantos km Rodados: '))
total = diaria * 60 + km * 0.15

print(f'O total a Pagar e de R${total:.2f}.')
