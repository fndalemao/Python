num = int(input('Digite um número: '))
f = 1
print(f'Calculando {num}! ', end='')
for i in range(num, 0, -1):
    print(f'{i}', end='')
    print('x' if i > 1 else '=', end='')
    f *= i
print(f)