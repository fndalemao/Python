import random
numpc = random.randrange(5)
#print(numpc)
num = float(input('O PC está pensando em um número entre 0 e 5, tente adivinhar: '))
if num == numpc:
    print('PARABÉNS VOCÊ ACERTOU!!')
else:
    print('QUE PENA, TENTE OUTRA VEZ!')
