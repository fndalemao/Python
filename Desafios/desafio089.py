boletim = list()
dados = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    boletim.append(dados[:])
    dados.clear()
    stop = str(input('Deseja continuar? [S/N] '))
    if stop in 'Nn':
        break
for i, b in enumerate(boletim):
    print(f'{i} {boletim[i][0]} {(boletim[i][1] + boletim[i][2])/2}')
nota = 0
while nota != 999:
    nota = int(input('Mostrar notas de qual aluno? (999 Interrompe) '))
    print(f'As notas de {boletim[nota][0]} são {boletim[nota][1:3]}')

print(boletim)