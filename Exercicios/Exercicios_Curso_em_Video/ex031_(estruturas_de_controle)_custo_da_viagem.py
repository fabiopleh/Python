# Custo da Viagem.

dist = float(input('Digite a Distânciada (Km) da sua Viagem: '))
passag = dist * 0.5 if dist <= 200 else dist * 0.45

print(f'O Valor da Passagem Será R${passag:.2f}')
