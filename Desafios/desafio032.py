ano = int(input('Digite um ano: '))
if (ano % 400 == 0) | (ano % 4 ==0) & (ano % 100 != 0):
    print('O ano de {} é BISSEXTO!'.format(ano))
else:
    print('O ano de {} não é BISSEXTO!'.format(ano))