qdegraus = int(input())
alturas = [int(x) for x in input().split()]

# inicio
primeira_pos = -1
for pos, altura in enumerate(alturas):
    if altura != -1:
        primeira_pos = pos
        break

for i in range(primeira_pos - 1, -1, -1):
    alturas[i] = alturas[i+1] + 1

# meio
ultima_pos = -1
pos_anterior = primeira_pos
for pos_atual in range(primeira_pos, qdegraus):
    if altura == -1: continue
    ultima_pos = pos_atual
    altura_anterior = alturas[pos_anterior]
    altura_atual = alturas[pos_atual]
    pos_pico = (pos_anterior + pos_atual + altura_atual - altura_anterior) / 2
    altura_pico = pos_pico - pos_anterior + altura_anterior

    for i in range(pos_anterior + 1, pos_atual):
        alturas[i] = int(-abs(i - pos_pico) + altura_pico)

for i in range(ultima_pos + 1, qdegraus):
    alturas[i] = alturas[i-1] + 1

print(*alturas, sep=' ')