soma = i = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    i += 1
    soma += num
print(f'A soma dos {i} valores foi {soma}!')