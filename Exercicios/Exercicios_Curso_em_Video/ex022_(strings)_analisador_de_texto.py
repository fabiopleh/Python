# Analizador de Texto.

nomecomp = input('Digite seu Nome Completo: ').strip()
lstnomecomp = nomecomp.split()

print('Analisando seu Nome...')
print(f'Nome em Maiusculas: {nomecomp.upper()}')
print(f'Nome em Minúsculas: {nomecomp.lower()}')
print(f"Tem {len(''.join(lstnomecomp))} Letras.")
print(f'Primeiro Nome, {lstnomecomp[0]}, {len(lstnomecomp[0])} Letras.')
