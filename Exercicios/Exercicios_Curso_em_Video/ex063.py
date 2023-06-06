# Sequência de Fibonacci.

cont = 0
n1 = 1
n2 = 0
sm = 0

print('~~' * 11)
print('Sequência de Fibonacci')
print('~~' * 11)

num = int(input('Quantos ter você quer mostrar? '))

while cont < num:
    print(sm, end=' - ')
    n1, n2 = sm, n1
    sm = n1 + n2
    cont += 1

print('FIM!')
