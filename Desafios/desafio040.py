n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'Sua média é {m:.2f}')
if m < 5:
    print('Você foi REPROVADO!')
elif m >= 5 and m <= 6.9:
    print('Você está de RECUPERAÇÃO!')
else:
    print('Você foi APROVADO!')