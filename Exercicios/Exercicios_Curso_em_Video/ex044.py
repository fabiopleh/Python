# Aplica Desconto ou Acrescimo

p = float(input('Valor da Compra: R$ '))
cp = int(input('Condição de Pagamento:\n'
               '[ 1 ] À Vista DINHEIRO/CHEQUE\n'
               '[ 2 ] À Vista no CARTÃO\n'
               '[ 3 ] 2x no CARTÃO\n'
               '[ 4 ] 3x no CARTÃO\n'
               'Digite sua Opção de Pagamento: '))

if cp == 1:
    total = p - (p / 100 * 10)
elif cp == 2:
    total = p - (p / 100 * 5)
elif cp == 3:
    total = p
    print(f'Sua Compra será Parcelada em 2x de R${(total / 2):.2f}')
elif cp == 4:
    total = p + (p / 100 * 20)
    print(f'Sua Compra será Parcelada em 3x de R${(total / 3):.2f}')
print(f'Sua Compra de R${p:.2f} terá o Valor Final de R${total:.2f}')
