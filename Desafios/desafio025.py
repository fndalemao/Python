nome = input('Digite seu nome completo: ')
nome = nome.strip()
if nome.upper().count('SILVA') >= 1:
    print('Você possui "Silva" em seu nome!')
else:
    print('Você não possui "Silva" em seu nome!')