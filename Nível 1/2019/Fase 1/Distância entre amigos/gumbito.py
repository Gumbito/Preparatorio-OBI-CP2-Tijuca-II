qpredios = int(input())
andares = [int(x) for x in input().split()]

def calc_dist(predio1: int, predio2: int) -> int:
    if predio1 == predio2: return -1
    return andares[predio1] + abs(predio1 - predio2) + andares[predio2]

ultima_max_dist = max(calc_dist(0, i) for i in range(1, qpredios))
allmax_dist = ultima_max_dist

for pos in range(1, qpredios - 1):
    nova_max_dist = (ultima_max_dist - (andares[pos - 1] + 1)) + andares[pos]
    allmax_dist = max(allmax_dist, nova_max_dist)
    ultima_max_dist = nova_max_dist

print(allmax_dist)

# oq q essa questão tá fazendo na fase 1 do nível 1