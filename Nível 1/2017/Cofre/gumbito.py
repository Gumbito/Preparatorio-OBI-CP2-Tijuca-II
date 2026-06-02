qposicoes, qdestinos = [int(x) for x in input().split()]
barra = [int(x) for x in input().split()]

prefix_aparicoes: list[list[int]] = [[0] * (len(barra) + 1) for _ in range(10)]
for pos, num in enumerate(barra, start=1):
    for i in range(10):
        prefix_aparicoes[i][pos] = prefix_aparicoes[i][pos - 1]
    prefix_aparicoes[num][pos] += 1

def calcular_aparicoes(num: int, l: int, r: int):
    return prefix_aparicoes[num][r] - prefix_aparicoes[num][l-1]

destinos = [int(x) for x in input().split()]
atual = 0
aparicoes = [0] * 10
for i in range(1, qdestinos):
    destino = destinos[i]
    direcao = 1 if atual < destino else -1
    l, r = sorted((atual + direcao, destino))
    for num in range(10):
        aparicoes[num] += calcular_aparicoes(num, l, r)
    atual = destino

print(*aparicoes)

# O(n+m), mas 40/100 :/