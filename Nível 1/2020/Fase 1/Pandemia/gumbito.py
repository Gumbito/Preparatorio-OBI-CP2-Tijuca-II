qamigos, qreunioes = [int(x) for x in input().split()]
paciente_zero, reuniao_infectada = [int(x) for x in input().split()]

# ignora as reunioes anteriores à infectada primeiro
id_reuniao = 1
while id_reuniao < reuniao_infectada:
    input()
    id_reuniao += 1

infectados = {paciente_zero}
for id_reuniao in range(id_reuniao, qreunioes + 1):
    reuniao = [int(x) for x in input().split()]
    qparticipantes = reuniao.pop(0)
    participantes = set(reuniao)
    # se não tiver nenhum infectado entre os participantes, pula essa reunião
    if participantes.isdisjoint(infectados): continue
    # senão, adiciona todos os participantes ao conjunto de infectados
    infectados = infectados.union(participantes)
    
print(len(infectados))

# amo sets