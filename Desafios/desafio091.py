from random import randint
from time import sleep
from operator import itemgetter
valores = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6), 'Jogador 3': randint(1, 6),'Jogador 4': randint(1, 6)}
ranking = dict()
print('Valores sorteados:')
for k, v in valores.items():
    print(f'O {k} tirou o valor {v} no dado.')
    sleep(0.8)
ranking = sorted(valores.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores'
      ':')
for i, v in enumerate(ranking):
    print(f'{i + 1}º Lugar: {v[0]} com {v[1]}')
