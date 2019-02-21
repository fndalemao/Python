def leiaInt(msg):
    global n
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            n = int(n)
            return n
        else:
            print('\33[0;31mERRO! Digite um número inteiro válido\33[m')
        if ok:
            break


n = leiaInt('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}.')