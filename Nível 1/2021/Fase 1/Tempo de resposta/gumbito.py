# tipos de registro:
# (eu quando deixo meu código legível:)
# ((coff coff))
INTERVALO_DE_TEMPO = 'T'
MENSAGEM_RECEBIDA =  'R'
MENSAGEM_ENVIADA =   'E'

class Amigo():
    def __init__(self):
        self.tempo_total_esperando: int = 0
        self.respondido: bool = False

qregistros = int(input())

amigos: dict[int, Amigo] = dict()

def espera(tempo):
    for amigo in amigos.values():
        if not amigo.respondido: 
            amigo.tempo_total_esperando += tempo

for _ in range(qregistros):
    registro = input().split()
    tipo_registro = registro[0]
    argumento = int(registro[1])

    if tipo_registro == INTERVALO_DE_TEMPO:
        tempo = argumento
        espera(tempo - 1)
        continue

    # espera o intervalo de tempo default entre dois registros de eventos consecutivos (1 segundo)
    espera(1) 

    id_amigo = argumento
    if tipo_registro == MENSAGEM_RECEBIDA:
        if id_amigo not in amigos: amigos[id_amigo] = Amigo()
        else: amigos[id_amigo].respondido = False
    elif tipo_registro == MENSAGEM_ENVIADA:
        amigos[id_amigo].respondido = True
    

for id_amigo, amigo in sorted(amigos.items(), key=lambda x: x[0]):
    print(f'{id_amigo} {amigo.tempo_total_esperando if amigo.respondido else -1}')

# ainda bem que a questão não manda mais de um registro de tempo seguido