# Aquele Clássico de Média.

n1 = float(input('Digite a Primeira Nota: '))
n2 = float(input('Digite a Segunda Nota: '))
media = (n1 + n2) / 2

print(f'Tirando {n1} e {n2}, a Média do Aluno é {media:.1f}.')

if media < 5:
    print('O Aluno está REPROVADO.')
elif 5 <= media < 7:
    print('O Aluno está em RECUPERAÇÃO.')
else:
    print('O Aluno está APROVADO.')
