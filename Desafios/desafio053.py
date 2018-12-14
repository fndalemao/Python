frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = '' #junto[::-1] dessa forma ele irá ler de trás para frente, sem precisar usar o for
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(f'{junto} ao contrário é {inverso}')
if junto == inverso:
    print('Temos um PALÍNDROMO!')
else:
    print('Não temos um PALÍNDROMO!')