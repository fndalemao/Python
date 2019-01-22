matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = somaCol = maior = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor na posição {[l, c]}: '))
        if  matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]
for c in range(3):
    print(matriz[c])
print(f'A soma de todos os números pares é {somaPar}')
for c in range(3):
    somaCol += matriz[c][2]
print(f'A soma dos valores da terceira coluna é {somaCol}')
for c in matriz[1]:
    if c > maior:
        maior = c
print(f'O maior valor digitado foi {maior}')