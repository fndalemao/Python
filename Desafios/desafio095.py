time = list()
jogador = dict()
gols = list()
while True:
    jogador.clear()
    print('-' * 30)
    jogador['nome'] = str(input('Nome: '))
    partidas = int(input('Quantas partidas você jogou? '))
    gols.clear()
    for p in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {p+1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        resp = str(input('Você quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar' ))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Jogador {busca} não encontrado.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'     No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('Volte Sempre!')
