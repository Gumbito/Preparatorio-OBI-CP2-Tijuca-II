from itertools import batched

qchocolates = int(input())
precos = [int(input()) for _ in range(qchocolates)]

# sort reverso porque depois eu vou popar os menores precos que sobraram (ficaram sem trio)
# daí popar no fim da lista é mais rápido que popar no início
precos.sort(reverse=True)
qresto = qchocolates % 3
preco_total = sum(precos.pop() for _ in range(qresto))

for trio in batched(precos, 3):
    preco_total += trio[0] + trio[1]

print(preco_total)