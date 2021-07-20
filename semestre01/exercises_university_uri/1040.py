valor = input().split()
a, b, c, d = valor
n1 = float(a) * 2
n2 = float(b) * 3
n3 = float(c) * 4
n4 = float(d) * 1
media1 = (n1 + n2 + n3 + n4) / 10
print(f'Media: {media1:.1f}')
if 5.0 <= media1 <= 6.9:
    print('Aluno em exame.')
    valor = input()
    e = valor
    exame = float(e)
    print(f'Nota do exame: {exame:.1f}')
    media2 = (exame + media1) / 2
    if media2 >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado')
    print(f'Media final: {media2:.1f}')
elif media1 >= 7.0:
    print('Aluno aprovado.')
elif media1 < 5.0:
    print('Aluno reprovado.')


