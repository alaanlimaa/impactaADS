x = int(input())
y = int(input())
soma = 0
if y < 0:
    for c in range(x, y, -1):
        if c % 2 != 0:
            soma += c
    print(soma)
elif x > y:
    for c in range(y, x):
        if c % 2 != 0:
            soma += c
    print(soma)
else:
    print('0')





