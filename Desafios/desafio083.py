expressao = str(input('Escreva sua expressão: '))
parent = list()
for c in expressao:
    if c == '(':
        parent.append(c)
    elif c == ')':
        if len(parent) > 0:
            parent.pop()
        else:
            parent.append(')')
            break
if len(parent) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')