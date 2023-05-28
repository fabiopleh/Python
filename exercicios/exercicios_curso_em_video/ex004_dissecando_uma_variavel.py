# Dissecando uma Variável.

algo = input('Digite Algo: ')

print('O tipo primitivo desse Valor é ', type(algo))
print('Só tem Espaços? ', algo.isspace())
print('É um Número? ', algo.isnumeric())
print('É Alfabético? ', algo.isalpha())
print('É Alfanumérico? ', algo.isalnum())
print('Está em Maiúsculas? ', algo.isupper())
print('Está em Minúsculas? ', algo.islower())
print('Está Capitalizada? ', algo.istitle())
