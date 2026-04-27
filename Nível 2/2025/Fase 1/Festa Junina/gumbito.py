escola, supermercado, lojinha = [int(input()) for _ in range(3)]

def dist(ponto1: int, ponto2: int) -> int:
    return abs(ponto1 - ponto2)

dist_total = 0
# tanto faz se ela vai primeiro pra lojinha ou pro supermercado
dist_total += dist(escola, supermercado)
dist_total += dist(supermercado, lojinha)
dist_total += dist(lojinha, escola)

print(dist_total)