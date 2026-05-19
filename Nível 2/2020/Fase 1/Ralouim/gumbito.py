coord = tuple[int, int]

qtendas = int(input())

def calc_dist(c1: coord, c2: coord) -> float:
    x1, y1 = c1
    x2, y2 = c2
    if (x1 == x2) and (y1 == y2): return 0.0
    dx, dy = abs(x1 - x2), abs(y1 - y2)
    return ((dx**2) + (dy**2)) ** (1/2)

tendas: list[coord] = []
for _ in range(qtendas):
    x, y = [int(c) for c in input().split()]
    tendas.append((x, y))

def mais_guloseimas() -> int:
    guloseimas_maximas = [0]
    def procura(origem: coord, raio: float, guloseimas_acumuladas: int = 1):
        guloseimas_maximas[0] = max(guloseimas_maximas[0], guloseimas_acumuladas)
        for tenda in tendas:
            dist = calc_dist(origem, tenda)
            if dist == 0: continue
            if dist >= raio: continue
            procura(tenda, dist, guloseimas_acumuladas + 1)

    for tenda in tendas:
        procura(tenda, calc_dist((0, 0), tenda))

    return guloseimas_maximas[0]

print(mais_guloseimas())