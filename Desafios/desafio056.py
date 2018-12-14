totIdade = 0
maiorIdadeHomem = 0
nomeVelho = 0
totMulher = 0
for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    totIdade += idade
    if idade > maiorIdadeHomem and sexo == 'M':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo == 'F' and idade < 20:
        totMulher += 1
mediaIdade = totIdade / 4
print(f'A média de idade do grupo é de {mediaIdade} anos.')
print(f'O nome do Homem mais velho é {nomeVelho} e ele tem {maiorIdadeHomem} anos.')
if totMulher == 0:
    print('Não temos mulheres menores de 20 anos no grupo')
else:
    print(f'Nesse grupo possuí {totMulher} mulheres menores de 20 anos.')