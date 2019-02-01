jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome: '))
jogador['partidas'] = int(input('Quantas partidas você jogou? '))
for p in range(jogador['partidas']):
    gols.append(int(input(f'Quantos gols na partida {p}? ')))
jogador['gols'] = gols[:]
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for p, i in enumerate(jogador['gols']):
    if p == 0:
        jogador['total'] = i
    else:
        jogador['total'] += i
    print(f'Na partida {p}, fez {i} gols.')
print(f'Foi um total de {jogador["total"]} gols.')