def ficha(jogador='<desconhecido>', gol=0):
    print(f'O jogador {jogador} fez {gol} gol(s) no campeonato.')


nome = str(input('Nome do jogador: '))
gol = str(input('Número de gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(gol=gol)
else:
    ficha(nome, gol)
