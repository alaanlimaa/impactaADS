soma = 0
while True:
    doacao = float(input())
    if doacao == -1.0:
        break
    soma += doacao
print(f'VC$ {soma:.2f}')
conversao = soma * 2.50
print(f'R$ {conversao:.2f}')
