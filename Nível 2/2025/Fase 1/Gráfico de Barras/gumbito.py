qbrinquedos = int(input())
lista = [int(x) for x in input().split()]
altura_grafico = max(lista)

for index_linha in range(altura_grafico):
    linha: list[int] = []
    for qpreferentes in lista:
        altura_linha = altura_grafico - index_linha
        linha.append(0 if altura_linha > qpreferentes else 1)
    # printa a linha com cada elemento separado por espaço
    print(*linha)