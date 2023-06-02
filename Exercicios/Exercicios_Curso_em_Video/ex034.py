# Recalculado Salário.
sal = float(input('Informe o Salário: R$'))
if sal > 1250:
    nsal = sal + (sal / 100 * 10)
else:
    nsal = sal + (sal / 100 * 15)
print(f'O Novo Salário será R${nsal}')
