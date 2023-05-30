# Pintando Parede.

largura = float(input('Largura da Parede: '))
altura = float(input('Altura da Parede: '))
area = largura * altura
tinta = area / 2

print(f'Sua parede tem a dimensão de {largura}m x {altura}m\n'
      f'E a área dela é de {area} m².\n'
      f'São Necessários {tinta:.1f}l de Tinta.')
