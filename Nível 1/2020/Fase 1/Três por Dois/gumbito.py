from itertools import batched

qchocolates = int(input())
precos = [int(input()) for _ in range(qchocolates)]

precos = ([0] * (3 - (qchocolates % 3))) + sorted(precos) # ordena a lista e garante que é divisível por 3 adicionando 0's no início
preco_total = 0
for trio in batched(precos, 3):
    preco_total += trio[1] + trio[2]

print(preco_total)

# tentei dar uma diferenciada na solução esperada