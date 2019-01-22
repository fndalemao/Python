galera = list()
dados = list()
maior = list()
menor = list()
totpessoas = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    stop = str(input('Quer continuar? [S/N] '))
    galera.append(dados[:])
    dados.clear()
    totpessoas += 1
    if stop in 'Nn':
        break
for p in galera:
    if p[1] == 100:
        maior.append(p[0])
    if p[1] == 70:
        menor.append(p[0])
print(f'As pessoas com maior peso são {maior} com 100 Kg.')
print(f'A pessoa com menor peso é {menor} com 70 Kg.')
print(f'No total foram {totpessoas} pessoas cadastradas.')