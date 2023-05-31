# Virifica altura quantidade de Letras 'altura',
# índice da primeira e última.
frase = input('Digite uma Frase: ').strip().lower()
print('A letra A aparece {} vezes'.format(frase.count('altura')))
print('A Primeira na Posição {}'.format(frase.find('altura')+1))
print('A Ultima na Posição {}'.format(frase.rfind('altura')+1))
