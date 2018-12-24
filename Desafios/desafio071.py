print('=-' * 15)
print('BANCO GRINGOTS')
print('=-' * 15)
saque = int(input('Qual valor você quer sacar? R$'))
ced50 = ced20 = ced10 = ced01 = 0
resto = saque
while resto != 0:
    if resto >= 50:
        ced50 = resto // 50
        resto = resto % 50
    if resto >= 20:
        ced20 = resto // 20
        resto = resto % 20
    if resto >= 10:
        ced10 = resto // 10
        resto = resto % 10
    if resto >= 1:
        ced01 = resto // 1
        resto = resto % 1
if ced50 > 0:
    print(f'Total de {ced50} cédulas de R$50')
if ced20 > 0:
    print(f'Total de {ced20} cédulas de R$20')
if ced10 > 0:
    print(f'Total de {ced10} cédulas de R$10')
if ced01 > 0:
    print(f'Total de {ced01} cédulas de R$1')