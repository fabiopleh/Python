# Aumentos Múltiplos.

sal = float(input('Informe o Salário: R$'))

if sal > 1250:
    novsal = sal + (sal / 100 * 10)
else:
    novsal = sal + (sal / 100 * 15)

print(f'O Novo Salário será R${novsal}')
