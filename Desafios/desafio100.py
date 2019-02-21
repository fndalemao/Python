from random import randint
from time import sleep
numeros = list()


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(5):
        numeros.append(randint(0, 9))
    for i in numeros:
        print(f'{i} ', end='')
        sleep(0.4)
    print('PRONTO')


def somaPar(*par):
    totpar = 0
    for i in numeros:
        if i % 2 == 0:
            totpar += i
    print(f'Somando os valores PARES de {numeros}, temos {totpar}.')


sorteia()
somaPar()
