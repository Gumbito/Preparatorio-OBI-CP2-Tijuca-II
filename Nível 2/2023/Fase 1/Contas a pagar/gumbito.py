dinheiro_vovo = int(input())
contas = [int(input()) for _ in range(3)]

contas.sort()

qpagas = 0
for conta in contas:
    dinheiro_vovo -= conta
    if dinheiro_vovo < 0: break
    qpagas += 1

print(qpagas)