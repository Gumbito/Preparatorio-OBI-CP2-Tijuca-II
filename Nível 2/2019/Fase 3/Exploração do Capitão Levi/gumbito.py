qtitans, p, q = [int(x) for x in input().split()]

coord = tuple[int, int]
titans: list[coord] = []
for _ in range(qtitans):
    x, y = [int(a) for a in input().split()]
    titans.append((x, y))

min_slope = p/q

def calcular_slope(a: coord, b: coord) -> float:
    xa, ya = a
    xb, yb = b
    return (ya - yb)/(xa - xb)

qpares = 0
for a in titans:
    for b in titans:
        if a == b: continue
        slope = calcular_slope(a, b)
        if slope >= min_slope:
            qpares += 1
qpares //= 2

print(qpares)