listnum = list()
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
listnum.sort()
print(f'Você digitou os valores {listnum}')