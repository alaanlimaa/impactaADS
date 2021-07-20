lista_item = list(map(int, input().split()))
geral = []
for i in lista_item:
    geral.append(i)
while True:
    acoes = input().split()
    if 'adicionar' in acoes:
        geral.append(int(acoes[1]))
    elif 'exibir' in acoes:
        print(*sorted(geral))
    elif 'remover' in acoes:
        if int(acoes[1]) in geral:
            geral.remove(int(acoes[1]))
        else:
            print(f'código {int(acoes[1])} não encontrado')
    elif 'encerrar' in acoes:
        if len(geral) == 0:
            print(" ")
            break
        else:
            print(*sorted(geral))
            break
