soma = 0
cont = 0
num = 0
num = int(input('Digite um número: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número: '))
print(f'Você digitou {cont} números e a soma entre eles é {soma}')