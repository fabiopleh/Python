#
r = 0
num = int(input('Digite um Número: '))

for c in range(1, num + 1):
    if num % c == 0:
       r += 1
print(f'O Número {num} foi Divisivel {r} Vezes.')
if r == 2:
   print('Então ele é Primo!')
else:
   print('Então ele Não é Primo!')
