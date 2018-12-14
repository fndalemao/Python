num = int(input('Digite um número inteiro: '))
cont = 0
for i in range(1, num + 1):
    if num % i == 0:
        cont = cont + 1
        print('\033[34m', end='')
    else:
        print('\033[31m', end='')
    print(f'{i}', end=' ')
print(f'\n\033[mO número {num} foi divisível {cont} vezes')
if cont > 2:
    print(f'\033[m{num} não é um número PRIMO!')
else:
    print(f'\033[m{num} é um número PRIMO!')