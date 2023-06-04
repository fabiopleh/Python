# Alistamento Militar.

from datetime import date

anonasc = int(input('Informe o Ano do seu Nascimento: '))
idade = date.today().year - anonasc

print(f'Quem Nasceu em {anonasc} tem {idade} Anos em {date.today().year}.')

if idade == 18:
    print('Você Deve se Alistar IMEDIATAMENTE.')
elif idade < 18:
    print(f'Ainda Faltam {18 - idade} Anos para o seu Alistamento.')
    print(f'Seu Alistamento Será em {anonasc + 18}.')
else:
    print(f'Já Passou {idade - 18} anos da Data do seu Alistamento.')
    print(f'Você Deveria ter se Alistado em {anonasc + 18}.')
