from collections import deque

AGUA = 'o'
PRATELEIRA = '#'
NADA = '.'
coord = tuple[int, int]

qlinhas, qcolunas = [int(x) for x in input().split()]

parede: list[list[str]] = []

origem_goteira: coord = (-1, -1)
for lin in range(qlinhas):
    linha = list(input())
    for col, char in enumerate(linha):
        if char == AGUA:
            origem_goteira = (lin, col)
    parede.append(linha)

abertas: deque[coord] = deque()
abertas.append(origem_goteira)
while abertas:
    y, x = abertas.popleft()
    parede[y][x] = AGUA
    if y + 1 >= qlinhas: continue

    embaixo = parede[y + 1][x]
    if embaixo == NADA:
        abertas.append((y + 1, x))
        continue

    for dx in (-1, 1):
        vx = x + dx
        if not (0 <= vx < qcolunas): continue
        if parede[y][vx] == NADA:
            abertas.append((y, vx))

print('\n'.join((''.join(linha) for linha in parede)))