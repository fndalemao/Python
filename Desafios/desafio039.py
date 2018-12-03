#Faça um programa que leia o ano de nascimento de um jovem e informe,de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
#se é hora de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
nasc = int(input('Informe seu ano de nascimento: '))
idade = 2018 - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em 2018.')
if idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o alistamento.\nSeu alistamento será em {nasc + 18}')
elif idade == 18:
    print('Você precisa fazer o alistamento neste ano!')
elif idade > 18:
    print(f'Você já deveria ter se alistado à {idade - 18} anos.\nSeu alistamento foi em {nasc + 18}')
else:
    print('ERROR!')