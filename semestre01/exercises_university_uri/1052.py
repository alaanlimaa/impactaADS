n = int(input())
cont = 0
while cont != n:
    meses = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
    cont += 1
print(f'{meses[cont - 1]}')

