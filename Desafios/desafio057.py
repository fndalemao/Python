sexo = str(input('Sexo [M/F]: ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Dados inválidos, por favor digite seu sexo [M/F]: ')).strip().upper()
print(f'Sexo {sexo} registrado com sucesso!')