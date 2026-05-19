TAMANHO_PEQUENO, TAMANHO_MEDIO = 1, 2
SIM, NAO = 'S', 'N'

qpremiados = int(input())
tamanhos_solicitados = [int(x) for x in input().split()]
p_produzidas = int(input())
m_produzidas = int(input())

p_solicitadas = m_solicitadas = 0
for tamanho_solicitado in tamanhos_solicitados:
    if tamanho_solicitado == TAMANHO_PEQUENO:
        p_solicitadas += 1
    else:
        m_solicitadas += 1

if p_produzidas >= p_solicitadas and m_produzidas >= m_solicitadas:
    print(SIM)
else:
    print(NAO)
