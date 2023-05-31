# Trabalhando com Strings.
nc = input('Digite seu Nome Completo: ').strip()
ncl = nc.split()
print('Analisando seu Nome...')
print(f'Nome em Maiusculas: {nc.upper()}')
print(f'Nome em Minúsculas: {nc.lower()}')
print(f"Tem {len(''.join(ncl))} Letras.")
print(f'Primeiro Nome, {ncl[0]}, {len(ncl[0])} Letras.')
