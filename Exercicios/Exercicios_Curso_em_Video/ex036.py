# Simulação de Financiamento.
vc = float(input('Digite o Valor da Casa: R$'))
sl = float(input('Digite o Salário do Comprador: R$'))
ap = float(input('Digite Quantos Anos quer Pagar: '))
vp = vc / (ap * 12)
ps = sl / 100 * 30

if ps >= vp:
    print('Financiamento Aprovado!!!')
    print(f'Você pagará {ap * 12:.0f} Parcelas de R${vp:.2f}.')
else:
    print('Infelizmente seu Financiamento não foi Aprovado.')
