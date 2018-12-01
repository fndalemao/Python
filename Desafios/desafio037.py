#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual a base de conversão:
#1 para binário
#2 para octal
#3 para hexadecimal
n = int(input('Digite um número inteiro: '))
print('Escolha a base de conversão: \n [1] Binário \n [2] Octal \n [3] Hexadecimal')
o = int(input('Sua opção: '))
if o == 1:
    print(f'{n} convertido para BINÁRIO é igual a {bin(n)[2:]}')
elif o == 2:
    print(f'{n} convertido para OCTAL é igual a {oct(n)[2:]}')
elif o == 3:
    print(f'{n} convertido para HEXADECIMAL é igual a {hex(n)[2:]}')
else:
    print(f'{n} OPÇÃO INVÁLIDA!')