listnum = list()
qtd = 0
while True:
    num = int(input('Digite um valor: '))
    if num in listnum:
        print('Valor duplicado! Não vou adicionar...')
    else:
        listnum.append(num)
        print('Valor adicionado com sucesso...')
        qtd += 1
    para = str(input('Você deseja continuar? (S/N) '))
    if para in 'Nn':
        break
listnum.sort(reverse=True)
print(f'Você digitou {qtd} valores')
print(f'Sua lista em ordem decrescente {listnum}')
if 5 in listnum:
    print(f'O número 5 foi digitado e está na posição {listnum.index(5) + 1}')
else:
    print('Você não digitou o valor 5 portanto ele não está na sua lista')