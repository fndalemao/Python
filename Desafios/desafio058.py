import random
numpc = random.randrange(10)
#print(numpc)
num = float(input('O PC está pensando em um número entre 0 e 10, tente adivinhar: '))
cont = 1
while num != numpc:
    cont += 1
    if num < numpc:
        num = float(input('MAIS, tente outra vez: '))
    else:
        num = float(input('MENOS, tente outra vez: '))
print(f'Parabéns vc ACERTOU com {cont} tentativas!')