qamigos, qreunioes = [int(x) for x in input().split()]
paciente_zero, reuniao_infectada = [int(x) for x in input().split()]

for _ in range(reuniao_infectada - 1): input() # ignora as reunioes anteriores à infectada primeiro

infectados = {paciente_zero}
for _ in range(qreunioes - reuniao_infectada + 1):
    reuniao = [int(x) for x in input().split()]
    qparticipantes = reuniao.pop(0)
    participantes = set(reuniao)
    if participantes.isdisjoint(infectados): continue
    infectados = infectados.union(participantes)
    
print(len(infectados))
