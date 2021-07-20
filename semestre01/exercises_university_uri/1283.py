num = int(input())
cont = 1
soma = num
lista = [num]
while num != 0:
    num = int(input())
    if num < 0:
        break
    lista.append(num)
    soma += num
    cont += 1
media = soma / cont
print(f'MEDIA: {media :.2f}')
for i in lista:
    if i < media:
        print(i)

