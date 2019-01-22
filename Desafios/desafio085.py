numeros = [[], []]
for c in range(7):
    num = int(input('Número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print(f'Números pares: {numeros[0]}')
print((f'Números ímpares: {numeros[1]}'))