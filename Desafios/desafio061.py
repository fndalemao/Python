num = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 1
while cont < 11:
    print(num, end=' ')
    num += razao
    cont += 1
print('ACABOU!')