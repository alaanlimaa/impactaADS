nota_trabalhos = float(input())
nota_prova = float(input())
media = (nota_trabalhos + nota_prova) / 2
if media >= 6:
    print('aprovado')
elif nota_trabalhos >= 2:
    print('talvez com a sub')
else:
    print('reprovado')