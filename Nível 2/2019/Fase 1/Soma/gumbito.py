qquadrados, soma_alvo = [int(x) for x in input().split()]

prefix = [0] + [int(x) for x in input().split()]
for i in range(1, len(prefix)):
    prefix[i] += prefix[i-1]

def calc_soma(l: int, r: int, prefix: list[int] = prefix) -> int:
    return prefix[r] - prefix[l - 1]

qretangulos = 0
for l in range(1, len(prefix)):
    for r in range(l, len(prefix)):
        if calc_soma(l, r) == soma_alvo:
            qretangulos += 1

print(qretangulos)