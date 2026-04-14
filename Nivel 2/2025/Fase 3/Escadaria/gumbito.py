qdegraus = int(input())
alturas = [int(x) for x in input().split()]

# pega as posições de todos os degraus cujas alturas são conhecidas
posicoes = [i for i in range(qdegraus) if alturas[i] > 0]
primeira_pos = posicoes[0]
ultima_pos = posicoes[-1]

# preenche a esquerda e direita da escadaria
for i in range(primeira_pos - 1, -1, -1):
    alturas[i] = alturas[i+1] + 1
for i in range(ultima_pos + 1, qdegraus):
    alturas[i] = alturas[i-1] + 1

# para cada posição conhecida (exceto a última):
for i in range(len(posicoes) - 1):
    pos_inicial = posicoes[i]
    altura_inicial = alturas[pos_inicial]

    pos_final = posicoes[i+1]
    altura_final = alturas[pos_final]

    for pos_atual in range(pos_inicial + 1, pos_final):
        altura_atual = alturas[pos_atual - 1]
        dist = pos_final - pos_atual
        
        for d in (1, 0, -1):
            diff_altura = altura_final - (altura_atual + d)
            if dist >= abs(diff_altura):
                altura_atual += d
                break
        
        alturas[pos_atual] = altura_atual

print(*alturas, sep=' ')

