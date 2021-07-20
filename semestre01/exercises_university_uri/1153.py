
n = int(input())
f = 1
for c in range(n, 0, -1):
    f *= c
    if c == 1:
        print(f'{c} = {f}')
    elif c != 1:
        print(f'{c} x ', end='')

