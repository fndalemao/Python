conti = 'S'
i = maior = menor = soma = 0
while conti == 'S':
    num = float(input('Digite um número: '))
    i += 1
    soma += num
    if i == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    conti = str(input('Quer continuar? [S/N]')).upper().strip()
media = soma / i
print(f'Você digitou {i} números e a média foi {media}\nO maior valor foi {maior} e o menor foi {menor}')