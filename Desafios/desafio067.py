while True:
    tab = int(input('Quer ver a tabuada de qual valor? '))
    if tab >= 0:
        for i in range(11):
            print(f'{tab} x {i} = {tab * i}')
    else:
        break
print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')