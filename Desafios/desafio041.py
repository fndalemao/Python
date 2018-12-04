from datetime import date
nasc = int(input('Qual é seu ano de nascimento: '))
idade = date.today().year - nasc
if idade < 9:
    print(f'Você tem {idade} anos, sua categoria é: MIRIM.')
elif idade < 14:
    print(f'Você tem {idade} anos, sua categoria é: INFANTIL.')
elif idade < 19:
    print(f'Você tem {idade} anos, sua categoria é: JUNIOR.')
elif idade < 25:
    print(f'Você tem {idade} anos, sua categoria é: SÊNIOR.')
else:
    print(f'Você tem {idade} anos, sua categoria é: MASTER.')