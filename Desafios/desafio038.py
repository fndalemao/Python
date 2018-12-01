#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#O primeiro valor é MAIOR
#O segundo valor é MAIOR
#Não existe valor maior, os dois são IGUAIS
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
c = n1 - n2
if c > 0:
    print(f'{n1} é MAIOR que {n2}')
elif c < 0:
    print(f'{n2} é MAIOR que {n1}')
elif c == 0:
    print(f'{n1} e {n2} são IGUAIS')
else:
    print('ERROR!')