from random import randint
print('=-' * 15)
print('PAR OU ÍMPAR')
print('=-' * 15)
cont = 0
while True:
    num = int(input('Diga um valor de 0 à 10: '))
    if num > 10:
        print('=-' * 15)
        print('NÚMERO INVÁLIDO!')
        print('=-' * 15)
        break
    pc = randint(0, 11)
    opcao = str(input('Par ou Ímpar? [P/I]')).upper().strip()
    if opcao not in 'PI':
        print('=-' * 15)
        print('OPÇÃO INVÁLIDA!')
        print('=-' * 15)
        break
    soma = num + pc
    res = ''
    if soma % 2 == 0:
        res = 'PAR'
        print('-' * 30)
        print(f'Você jogou {num} e o computador jogou {pc}. Total de {soma} deu PAR!')
        print('-' * 30)
    else:
        res = 'IMPAR'
        print('-' * 30)
        print(f'Você jogou {num} e o computador jogou {pc}. Total de {soma} deu ÍMPAR!')
        print('-' * 30)
    if opcao == res.strip()[0]:
        print('Você GANHOU!')
        cont += 1
    else:
        print('Você PERDEU!')
        print('-' * 30)
        break
print(f'GAME OVER! VOCÊ VENCEU {cont} VEZES.')