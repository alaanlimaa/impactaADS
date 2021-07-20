def intervalo(n):
    int = ('[0,25]', '(25,50]', '(50,75]', '(75,100]')
    if 0 <= n <= 25:
        return f'Intervalo {int[0]}'
    elif 25 < n <= 50:
        return f'Intervalo {int[1]}'
    elif 50 < n <= 75:
        return f'Intervalo {int[2]}'
    elif 75 < n <= 100:
        return f'Intervalo {int[3]}'
    else:
        return 'Fora de intervalo'


num = float(input())
print(intervalo(num))

