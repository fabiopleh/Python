# Estatísticas em produtos.

total = mmil = 0
continuar = ' '

print('-' * 30)
print('{:^30}'.format('LOJA EX PYTHON'))
print('-' * 30)

while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço do Produto: R$'))

    total += preco

    if preco > 1000:
        mmil += 1

    if continuar == ' ' or preco < mbat:
        mbat = preco
        nmb = produto

    continuar = str(input('Quer Continuar? [S/N]: ')).strip().upper()[0]

    while not continuar in 'SN':
        continuar = str(input('Valor Invalido.\n'
                              'Quer Continuar? [S/N: ')).strip().upper()[0]
    if continuar == 'N':
            break

print('{:-^30}'.format(' FIM DO PROGRAMA '))
print(f'O Total da Compra Foi R${total:.2f}')
print(f'Temos {mmil} Produtos Custando mais de R$1000.00')
print(f'O Produto mais Barato foi {nmb} que Custa R${mbat:.2f}')
