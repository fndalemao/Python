for n in range(6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        num += num
print(f'A soma de todos os números pares digitados é {num}')