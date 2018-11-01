from math import sqrt
import emoji
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadrada de {} é {:.2f}'.format(num, raiz), end=' ')
print(emoji.emojize(':sunglasses:', use_aliases=True))