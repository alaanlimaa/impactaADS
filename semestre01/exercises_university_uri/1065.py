a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
valores = (a, b, c, d, e)
soma = 0
for c in valores:
    if c % 2 == 0:
        soma += 1
print(f'{soma} valores pares')

