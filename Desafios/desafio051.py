num = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = num + (10 - 1) * razao
for i in range(num, decimo + razao, razao):
    print(i, end=' ')
print('ACABOU!')