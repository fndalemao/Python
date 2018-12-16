print('-' *22)
print('SEQUÊNCIA DE FIBONACCI')
print('-' *22)
termo = int(input('Quantos termos você quer mostrar? '))
cont = 3
t1 = 0
t2 = 1
print(f'{t1} {t2} ', end= '')
while cont <= termo:
    t3 = t1 + t2
    print(t3, end= ' ')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')