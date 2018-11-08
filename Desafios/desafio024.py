cidade = input('Digite o nome da sua cidade: ')
cidade = cidade.strip()
cidade = cidade.upper()
dividido = cidade.split()
if dividido[0] == 'SANTO':
   print('Sua cidade começa com a palavra "Santo"')
else:
    print('Sua cidade não começa com a palavra "Santo"')
