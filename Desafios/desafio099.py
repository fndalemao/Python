from time import sleep
from random import randint


def maior(*num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    m = tot = 0
    for c, i in enumerate(num):
        if c == 0:
            m = i
        else:
            if i > m:
                m = i
        tot += 1
        print(f'{i} ', end='')
        sleep(0.4)
    print(f'Foram informados {tot} valores no total.')
    print(f'O maior valor informado foi {m}.')


maior(randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior(randint(1, 10), randint(1, 10), randint(1, 10))
maior(randint(1, 10), randint(1, 10))
maior()
