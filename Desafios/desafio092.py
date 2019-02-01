from datetime import datetime
pessoa = dict()
pessoa['Nome'] = str(input('Nome: '))
nasc = int(input('Anos de nascimento: '))
pessoa['Idade'] = datetime.now().year - nasc
pessoa['Ctps'] = int(input('Carteira de trabalho: (0 não tem) '))
if pessoa['Ctps'] != 0:
    pessoa['Ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: R$ '))
    pessoa['Idade a aposentar'] = (pessoa['Ano de contratação'] - nasc) + 35
for k, v in pessoa.items():
    print(f'{k}: {v}')