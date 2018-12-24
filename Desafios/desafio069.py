mais18 = mulherMenos18 = totHomem = 0
while True:
    print('-' * 30)
    print('CADASTRO DE PESSOAS')
    print('-' * 30)
    idade = int(input('Idade: '))
    if idade > 18:
        mais18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()
    if sexo in 'M':
        totHomem += 1
    if idade < 20 and sexo in 'F':
        mulherMenos18 += 1
    conti = ' '
    while conti not in 'SN':
        print('-' * 30)
        conti = str(input('Quer continuar? [S/N]] ')).upper()
        print('-' * 30)
    if conti == 'N':
        break
print(f'Temos {mais18} pessoa(s) com mais de 18 anos.')
print(f'Ao todo temos {totHomem} homem(s) cadastrados.')
print(f'E temos {mulherMenos18} mulher(s) com menos de 20 anos.')