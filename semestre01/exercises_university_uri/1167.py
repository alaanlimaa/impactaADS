inicio = int(input())
fim = int(input())
cont = 0
for c in range(inicio, fim + 1):
    if c % 4 == 0 and c % 100 != 0 or c % 400 == 0:
        print(c)
        cont += 1
print(f'bissextos: {cont}')
