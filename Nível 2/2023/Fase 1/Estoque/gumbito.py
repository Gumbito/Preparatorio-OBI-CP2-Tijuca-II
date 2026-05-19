qtipos, qtamanhos = [int(x) for x in input().split()]

quantidades: list[list[int]] = []

for _ in range(qtipos):
    linha = [int(x) for x in input().split()]
    quantidades.append(linha)

qvendas = 0
qpedidos = int(input())
for _ in range(qpedidos):
    tipo, tamanho = [int(x) - 1 for x in input().split()]
    quantidade = quantidades[tipo][tamanho]
    if quantidade > 0:
        quantidades[tipo][tamanho] -= 1
        qvendas += 1

print(qvendas)