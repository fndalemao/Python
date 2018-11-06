nome = input('Digite seu nome completo: ')
dividido = nome.split()
print('Bem vindo(a) {} {}'.format(dividido[0], dividido[len(dividido)-1]))