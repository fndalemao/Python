tabela = ('Corinthians', 'Internacional', 'Goiás', 'Palmeiras', 'Fluminense', 'Atlético-PR', 'Paraná', 'Cruzeiro', 'Botafogo', 'Santos', 'São Paulo', 'Vasco da Gama', 'Fortaleza', 'Juventude', 'Flamengo', 'Figueirense', 'São Caetano', 'Ponte Preta', 'Coritiba', 'Atlético-MG')
opcao = 0
while opcao < 1 or opcao > 5:
    print('TABELA DO BRASILEIRÃO:\n[1] Vinte Primeiros\n[2] Cinco Primeiros\n[3] Quatro Últimos\n[4] Vinte Primeiros em ordem alfabética\n[5] Posição do São Paulo')
    opcao = int(input('Digite uma opção: '))
if opcao == 1:
    for pos, time in enumerate(tabela):
        print(f'{pos + 1}º {time}')
if opcao == 2:
    for pos, time in enumerate(tabela[:5]):
        print(f'{pos + 1}º {time}')
if opcao == 3:
    for pos, time in enumerate(tabela[-4:]):
        print(f'{pos + 17}º {time}')
if opcao == 4:
    for pos, time in enumerate(sorted(tabela)):
        print(f'{pos + 1}º {time}')
if opcao == 5:
    print(f'O {tabela[10]} está na {tabela.index("São Paulo") + 1}ª posição')