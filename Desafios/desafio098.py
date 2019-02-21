from time import sleep


def contador(i, f, p):
    print('-=' * 20)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    c = i
    if c < f:
        while c <= f:
            print(f'{c} ', end='')
            sleep(0.5)
            c += p
    else:
        while c >= f:
            print(f'{c} ', end='')
            sleep(0.5)
            c -= p
    print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
n1 = int(input('Início: '))
n2 = int(input('Fim: '))
n3 = int(input('Passo: '))
contador(n1, n2, n3)
