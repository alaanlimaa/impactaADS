n1 = int(input())
n2 = int(input())
if n1 <= n2:
    m = n1
    while m < n2 + 1:
        for i in range(1, 11):
            print(f'{m} x {i} = { i * m}')
        print('----------')
        m += 1
else:
    print('Nenhuma tabuada no intervalo!')
