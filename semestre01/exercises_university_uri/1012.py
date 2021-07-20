valor = input().split()
a, b, c = valor
pi = 3.14159

triangulo = (float(a) * float(c))/2
circulo = pi * (float(c) * float(c))
trapezio = float(c) * (float(a) + float(b)) / 2
quadrado = float(b) * float(b)
retangulo = float(a) * float(b)

print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retangulo:.3f}')