# Verifica se é Masculino ou Feminino.

sexo = str(input('Informe Seu Sexo [M/F]: ')).upper().strip()[0]

while sexo not in 'MmFf':
    se_us = str(input('Opção Invalida.\n'
                      'Por Favor, Informe seu Sexo: ')).upper().strip()[0]

if sexo in 'Mm':
    print('Sexo Masculino Registrado.')
else:
    print('Sexo Feminino Registrado.')
