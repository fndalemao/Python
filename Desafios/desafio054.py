from datetime import date
menor = 0
maior = 0
for i in range(1, 8):
    ano = int(input('Digite o ano de nascimento da'+ ' ' + str(i) + '° pessoa: '))
    if date.today().year - ano < 18:
        menor += 1
    else:
        maior += 1
print(f'\nAo todo tivemos {maior} pessoas maiores de idade\nE também tivemos {menor} pessoas menores de idade.')