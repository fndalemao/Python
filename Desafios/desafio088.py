from random import randint
palpite = list()
qtdJogos = int(input('Quantos jogos você deseja gerar? '))
for i in range(qtdJogos):
    print(f'Jogo {i + 1}: ', end='')
    for n in range(6):
        palpite.append(randint(1, 60))
    palpite.sort()
    print(palpite)
    palpite.clear()