geral = []
while True:
    lista_item = list(map(str, input().split()))
    for i in lista_item:
        if i.isnumeric() and 'remover' not in lista_item:
            geral.append(int(i))
        elif i.isnumeric() and 'adicionar' in lista_item:
            geral.append(int(i))
        elif i == 'exibir':
            print(*sorted(geral))
    if 'remover' in lista_item and int(lista_item[1]) in geral:
        geral.remove(int(lista_item[1]))
    elif 'remover' in lista_item and int(lista_item[1]) not in geral:
        print(f'código {lista_item[1]} não encontrado')
    if 'encerrar' in lista_item:
        if len(geral) == 0:
            break
        else:
            print(*sorted(geral))
            break



