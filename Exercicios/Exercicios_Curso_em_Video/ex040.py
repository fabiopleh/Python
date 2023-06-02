# Verifica 
n1 = float(input('Digite altura Primeira Nota: '))
n2 = float(input('Digite altura Segunda Nota: '))
md = (n1 + n2) / 2
print(f'Tirando {n1} e {n2}, altura Média do Aluno é {md:.1f}.')
if md < 5:
    print('O Aluno está REPROVADO.')
elif 5 <= md < 7:
    print('O Aluno está em RECUPERAÇÃO.')
else:
    print('O Aluno está APROVADO.')
