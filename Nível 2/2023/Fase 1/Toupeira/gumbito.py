qsaloes, qtuneis = [int(x) for x in input().split()]

conectados_ao_salao: dict[int, set[int]] = dict()

for _ in range(qtuneis):
    salao1, salao2 = [int(x) for x in input().split()]
    if not salao1 in conectados_ao_salao: conectados_ao_salao[salao1] = set()
    if not salao2 in conectados_ao_salao: conectados_ao_salao[salao2] = set()
    conectados_ao_salao[salao1].add(salao2)
    conectados_ao_salao[salao2].add(salao1)

qcaminhos_validos = 0
qcaminhos_sugeridos = int(input())
for _ in range(qcaminhos_sugeridos):
    qtuneis, *tuneis = [int(x) for x in input().split()]
    for i in range(len(tuneis) - 1):
        atual, proximo = tuneis[i], tuneis[i+1]
        if proximo not in conectados_ao_salao[atual]:
            break
    else: qcaminhos_validos += 1

print(qcaminhos_validos)