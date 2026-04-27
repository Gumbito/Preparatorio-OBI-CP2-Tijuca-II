from sys import setrecursionlimit
# aumenta o limite de recursão para o máximo possível
setrecursionlimit(2**31 - 1)

qlinhas, forca = [int(x) for x in input().split()]
qcolunas = qlinhas

altitudes = [[int(c) for c in input()] for _ in range(qlinhas)]

def espalhar(coord: tuple[int, int] = (0, 0)) -> None: 
    y, x = coord
    if altitudes[y][x] > forca: return

    altitudes[y][x] = -1 # -1 = '*'
    for dy, dx in ((-1, 0), (0, -1), (1, 0), (0, 1)):
        vy, vx = y + dy, x + dx
        if not (0 <= vy < qlinhas): continue
        if not (0 <= vx < qcolunas): continue
        if altitudes[vy][vx] == -1: continue
        espalhar((vy, vx))

espalhar()


for altitudes_linha in altitudes:
    for altitude in altitudes_linha:
        char = '*' if altitude == -1 else str(altitude)
        print(char, end='') # printa cada caractere separadamente
    print() # pula linha

# não sabia que floodfill caia no nível 1