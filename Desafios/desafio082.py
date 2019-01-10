listnum = list()
listpar = list()
listimpar = list()
while True:
    num = int(input('Digite um valor: '))
    if num in listnum:
        print('Valor duplicado! Não vou adicionar...')
    else:
        listnum.append(num)
        print('Valor adicionado com sucesso...')
    para = str(input('Você deseja continuar? (S/N) '))
    if para in 'Nn':
        break
for n in listnum:
    if n % 2 == 0:
        listpar.append(n)
    else:
        listimpar.append(n)
print(f'A lista completa é {listnum}')
print(f'A lista de pares é {listpar}')
print(f'A lista de ímpares é {listimpar}')