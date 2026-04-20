LARGURA = 160
ALTURA = 70
area_total = LARGURA * ALTURA
metade_area_total = area_total / 2

base, topo = [int(input()) for _ in range(2)]

media_bases: float = (base + topo) / 2
pedaco1 = media_bases * ALTURA # area do trapézio

if   pedaco1 > metade_area_total: print(1)
elif pedaco1 < metade_area_total: print(2)
else:                             print(0)

# Obs.: não tem floating-point imprecision aqui porque as divisões são sempre por 2 e o numerador é sempre inteiro e pequeno suficiente
