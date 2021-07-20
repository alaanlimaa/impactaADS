div = int(input())
pag = int(input())
pgto = 1
while True:
    if div < pag:
        print(f'pagamento: {pgto}')
        pgto += 1
        print(f'antes = {div}')
        print(f'depois = 0')
        print('-----')
        break
    print(f'pagamento: {pgto}')
    pgto += 1
    print(f'antes = {div}')
    div = div - pag
    print(f'depois = {div}')
    print('-----')
    if div == 0:
        break

