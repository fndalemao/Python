palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalho', 'mercado', 'programador', 'futuro')
for p in range(len(palavras)):
    print(f'\nNa palavra {palavras[p].upper()} temos', end=' ')
    for l in palavras[p]:
        if l == 'a': #if l in 'aeiouy' também da certo e utiliza menos linhas
            print(l, end=' ')
        if l == 'e':
            print(l, end=' ')
        if l == 'i':
            print(l, end=' ')
        if l == 'o':
            print(l, end=' ')
        if l == 'u':
            print(l, end=' ')
        if l == 'y':
            print(l, end=' ')