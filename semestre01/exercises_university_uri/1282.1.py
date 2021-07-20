def txt(msg):
    print('-' * len(msg))
    print(msg)
    print('-' * len(msg))


qtdCanais = int(input())
lista = []
for c in range(1, qtdCanais + 1):
    num = input()
    if ' ' in num:
        numE = num.replace(' ', '-')
        numE = numE.replace(';', ' ').split()
        lista.append(numE)
    else:
        num = num.replace(';', ' ').split()
        lista.append(num)
premium = float(input())
notPremium = float(input())
txt('BÔNUS')
for s in lista:
    insc = int(s[1])
    mont = float(s[2])
    div = insc % 1000
    if 'não' in s:
        if insc > 1000 and div > 0:
            totInsc = insc - div
            monetizar = ((totInsc / 1000) * notPremium) + mont
        elif insc < 1000 and div > 0:
            monetizar = float(s[2])
        elif div == 0:
            monetizar = ((insc / 1000) * notPremium) + mont
    else:
        if insc > 1000 and div > 0:
            totInsc = insc - div
            monetizar = ((totInsc / 1000) * premium) + mont
        elif insc < 1000 and div > 0:
            monetizar = float(s[2])
        elif div == 0:
            monetizar = ((insc / 1000) * premium) + mont
    if '-' in str(s[0]):
        print(f'{str(s[0]).replace("-", " ")}: R$ {monetizar:.2f}')
    else:
        print(f'{s[0]}: R$ {monetizar:.2f}')

