# Radar Eletrônico.

vel = int(input('Qual a Velocidade do Carro? '))

if vel > 80:
    print('Limite de Velocidade Excedido!')
    print(f'Você foi Multado em R${(vel - 80) * 7:.2f}')
    
print('Tenha um bom dia! Dirija com Segurança!')
