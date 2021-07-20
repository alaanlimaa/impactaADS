preco = float(input())
qtd = int(input())
desconto = 0.10 + (qtd * 0.01)
total = preco * qtd
total_com_desc = total - (total * desconto)
print(f'{total:.2f}')
print(f'{total_com_desc:.2f}')