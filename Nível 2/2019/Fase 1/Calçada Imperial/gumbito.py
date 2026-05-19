tamanho = int(input())

calcada: list[int] = []

# guarda os números tirando os repetidos seguidos
ultimo = -1
for _ in range(tamanho):
    num = int(input())
    if num == ultimo: continue
    calcada.append(num)
    ultimo = num

if len(calcada) == 1:
    print(1)
    exit()

tamanho_max = 0
vistos: set[int] = set()
for i in range(len(calcada) - 1):
    num = calcada[i]
    if num in vistos:
        continue
    vistos.add(num)
    
    for j in range(i + 1, len(calcada)):
        par = (num, calcada[j])
        # index do ultimo valor encontrado do par (0 ou 1)
        index_ultimo = 1
        # x ^ 1 com x valendo 0 ou 1, simplesmente inverte
        # i.e. 0 vira 1 e 1 vira 0

        # calculando o tamanho da sequencia do par
        tamanho_atual = 2
        for k in range(j + 1, len(calcada)):
            atual = calcada[k]
            if atual == par[index_ultimo ^ 1]:
                tamanho_atual += 1
                index_ultimo ^= 1

        tamanho_max = max(tamanho_max, tamanho_atual)

print(tamanho_max)