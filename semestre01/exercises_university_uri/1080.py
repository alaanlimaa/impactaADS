lista = []
maior = 0
for c in range(0, 10):
    lista.append(int(input()))
    if c == 0:
        maior = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
print(maior)
print(lista.index(maior) + 1)






