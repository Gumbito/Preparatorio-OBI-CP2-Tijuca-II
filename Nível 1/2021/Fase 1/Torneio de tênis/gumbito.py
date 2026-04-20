QJOGOS = 6
VITORIA = 'V'
qvitorias: int = 0
for _ in range(QJOGOS):
    if input() == VITORIA: qvitorias += 1

grupo: int = -1
if   qvitorias >= 5: grupo = 1
elif qvitorias >= 3: grupo = 2
elif qvitorias >= 1: grupo = 3

print(grupo)