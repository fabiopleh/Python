# Aprovando Empréstimo.

vcasa = float(input('Digite o Valor da Casa: R$'))
sal = float(input('Digite o Salário do Comprador: R$'))
anospag = float(input('Digite Quantos Anos quer Pagar: '))
vprest = vcasa / (anospag * 12)
pcsal = sal / 100 * 30

if pcsal >= vprest:
    print('Financiamento Aprovado!!!')
    print(f'Você pagará {anospag * 12:.0f} Parcelas de R${vprest:.2f}.')
else:
    print('Infelizmente seu Financiamento não foi Aprovado.')
