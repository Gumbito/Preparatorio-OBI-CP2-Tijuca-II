n = int(input())
qsimbolos = n + 1

# 1 + 2 + 3 + ... + (qsimbolos - 1) + qsimbolos = triangular(qsimbolos)
qpecas = ((qsimbolos) * (qsimbolos + 1)) // 2

print(qpecas)