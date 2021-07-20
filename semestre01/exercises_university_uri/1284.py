alunos = int(input())
notas = []
finais = []
for n in range(1, alunos + 1):
    notasOriginal = float(input())
    notas.append(notasOriginal)
notaAlt = 0
for a in range(alunos + 1, (alunos * 2) + 1):
    notaAtividade = float(input())
    notas.append(notaAtividade)
    if notaAtividade == 10 and notas[a - (alunos + 1)] != 10:
        final = notas[a - (alunos + 1)] + 2
        if final > 10:
            final = float(10)
        finais.append(final)
        notaAlt += 1
    else:
        finais.append(notas[a - (alunos + 1)])
print(f'NOTAS ALTERADAS: {notaAlt}')
for i, a in enumerate(finais):
    if a == notas[i]:
        if a == notas[i] == 10:
            print(f'-(00{i + 1}) original: {notas[i]:.2f} | final: {notas[i]:.2f}')
        else:
            print(f'-(00{i + 1}) original: {f"0{notas[i]:.2f}"} | final: {f"0{notas[i]:.2f}"}')
    else:
        if notas[i + alunos] == 10 and a != notas[i]:
            if notas[i + alunos] == a == 10 and a != notas[i]:
                print(f'*(00{i + 1}) original: {f"0{notas[i]:.2f}"} | final: {a:.2f}')
            else:
                print(f'*(00{i + 1}) original: {f"0{notas[i]:.2f}"} | final: {f"0{a:.2f}"}')
