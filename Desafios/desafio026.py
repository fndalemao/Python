frase = input('Digite uma frase qualquer: ')
frase.strip()
print('Sua frase possui {} letras "A"'.format(frase.upper().count('A')))
print('A primeira letra "A" aparece na posição {} da sua frase'.format(frase.upper().find('A')))
print('A última letra "A" aparece na posição {} da sua frase'.format(frase.upper().rfind('A')))