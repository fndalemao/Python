listnum = list()
for c in range(5):
    num = int(input('Digite um número: '))
    if c == 0 or num > listnum[-1]:
        listnum.append(num)
    else:
        pos = 0
        while pos < len(listnum):
            if num <= listnum[pos]:
                listnum.insert(pos, num)
                break
            pos += 1
print(listnum)