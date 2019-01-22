matriz = [[], [], []], [[], [], []], [[], [], []]
for c, m in enumerate(matriz):
    for i, n in enumerate(matriz[c]):
        pos = int(input(f'Digite um valor na posição {[c, i]}: '))
        matriz[c][i].append(pos)
for c, m in enumerate(matriz):
    print(matriz[c])