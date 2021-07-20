dias_semana = ('domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado')
dia = str(input()).strip().lower()
prazo = int(input())
compradia = dias_semana.index(dia)
if prazo == 0:
    print('chega hoje!')
else:
    entrega = dias_semana[(compradia + prazo) % len(dias_semana)]
    print(f'sera entregue {entrega}')

print((compradia + prazo) % len(dias_semana))