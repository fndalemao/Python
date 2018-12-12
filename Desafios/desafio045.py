from random import randint
from time import sleep
lista = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
print('==========JO-KEN-PO==========')
user = int(input('Escolha:\n[0] PEDRA\n[1] PAPEL\n[2] TESOURA\n'))
if 0 <= user < 3:
    print('JO')
    sleep(0.7)
    print('KEN')
    sleep(0.7)
    print('PO!')
    print(f'O computador escolheu {lista[pc]}')
    print(f'Você escolheu {lista[user]}')
    if user == pc:
        print('EMPATE!')
    if pc == 0:
        if user == 1:
            print('PARABÉNS VOCÊ GANHOU!')
        elif user == 2:
            print('VOCÊ PERDEU, TENTE OUTRA VEZ')
    elif pc == 1:
        if user == 0:
            print('VOCÊ PERDEU, TENTE OUTRA VEZ')
        elif user == 2:
            print('PARABÉNS VOCÊ GANHOU!')
    elif pc == 2:
        if user == 0:
            print('PARABÉNS VOCÊ GANHOU!')
        elif user == 1:
            print('VOCÊ PERDEU, TENTE OUTRA VEZ')
else:
    print('OPÇÃO INVÁLIDA!')