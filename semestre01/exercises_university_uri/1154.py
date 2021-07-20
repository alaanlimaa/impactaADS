soma = idade = 0
cont = -1
while True:
    soma += idade
    cont += 1
    idade = int(input())
    if idade < 0:
        break
print(f'{(soma / cont):.2f}')
