# Calculando Descontos.

precoatual = float(input('Informe o Preço do Produto: R$'))
preconovo = precoatual - (precoatual / 100 * 5)
print(f'O Novo Preço do Produto é de R${preconovo:.2f}.')
