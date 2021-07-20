i = int(input())
f = int(input())
somaP = 0
for c in range(i, f + 1):
    cont = 1
    tot = 0
    while cont <= c:
        if c % cont == 0:
            tot += 1
        cont += 1
    if tot == 2:
        print(c)
        somaP += 1
print(f'primos: {somaP}')









