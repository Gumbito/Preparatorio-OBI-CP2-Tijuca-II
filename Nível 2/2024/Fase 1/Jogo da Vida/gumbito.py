VIVA = True
MORTA = False
coord = tuple[int, int]
matriz_estados = list[list[bool]]

tamanho, qpassos = [int(x) for x in input().split()]

celulas: matriz_estados = []
for _ in range(tamanho):
    celulas.append([bool(int(s)) for s in input()])

def str_celulas(celulas: matriz_estados) -> str:
    return '\n'.join((''.join((str(int(s)) for s in linha)) for linha in celulas))

def proximo_estado_regra(estado_atual: bool, qvizinhas_vivas: int) -> bool:
    if estado_atual == MORTA:
        return qvizinhas_vivas == 3
    return qvizinhas_vivas in {2, 3}

def proximo_estado_celula(coordinate: coord, celulas: matriz_estados) -> bool:
    y, x = coordinate
    qvizinhas_vivas = 0
    for dy in (-1, 0, 1):
        vy = y + dy
        if not (0 <= vy < tamanho): continue
        for dx in (-1, 0, 1):
            if dx == 0 and dy == 0: continue
            vx = x + dx
            if not (0 <= vx < tamanho): continue
            if celulas[vy][vx] == VIVA:
                qvizinhas_vivas += 1

    estado_dessa_celula = celulas[y][x]
    return proximo_estado_regra(estado_dessa_celula, qvizinhas_vivas)

def proxima_matriz_estados(celulas: matriz_estados) -> matriz_estados:
    novas_celulas: matriz_estados = [[False] * tamanho for _ in range(tamanho)]
    for y in range(tamanho):
        for x in range(tamanho):
            novas_celulas[y][x] = proximo_estado_celula((y, x), celulas)
    return novas_celulas

def simular_passos(qpassos: int, celulas: matriz_estados) -> matriz_estados:
    for _ in range(qpassos):
        celulas = proxima_matriz_estados(celulas)
    return celulas

print()
print(str_celulas(simular_passos(qpassos, celulas)))

