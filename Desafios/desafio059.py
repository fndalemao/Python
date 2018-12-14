from time import sleep
numeros = True
while numeros == True:
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    numeros = False
    menu = True
    while menu == True:
        print(
        '''    
        ----- MENU -----
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números
        [5] Sair do programa''')
        o = int(input('>>>>> Qual é a sua opção? '))
        if o == 1:
            print(f'{n1} + {n2} = {n1+n2}')
        elif o == 2:
            print(f'{n1} X {n2} = {n1*n2}')
        elif o == 3:
            if n1 > n2:
                print(f'{n1} é maior que {n2}')
            elif n1 < n2:
                print(f'{n2} é maior que {n1}')
            elif n1 == n2:
                print('Os números são iguais')
        elif o == 4:
            menu = False
            numeros = True
        elif o == 5:
            menu = False
            numeros = False
            print('Finalizando...')
            sleep(3)
            print('Programa finalizado, volte sempre!')