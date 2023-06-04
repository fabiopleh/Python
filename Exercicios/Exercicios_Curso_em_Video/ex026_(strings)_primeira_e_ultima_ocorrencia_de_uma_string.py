# Primeira e Última Ocorrência de uma String.

frase = input('Digite uma Frase: ').strip().lower()

print('A letra A aparece {} vezes'.format(frase.count('a')))
print('A Primeira na Posição {}'.format(frase.find('a')+1))
print('A Ultima na Posição {}'.format(frase.rfind('a')+1))
