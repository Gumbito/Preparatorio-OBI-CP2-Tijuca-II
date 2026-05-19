from sys import setrecursionlimit
setrecursionlimit((2**31) - 1)

qcidades = int(input())

class Cidade:
    def __init__(self, id: int):
        self.id = id
        self.conexoes: list[Conexao] = []

class Conexao:
    def __init__(self, destino: Cidade, empresa: bool):
        self.destino = destino
        self.empresa = empresa

cidades: list[Cidade] = [Cidade(i) for i in range(qcidades + 1)]
for _ in range(qcidades - 1):
    id1, id2, _empresa = [int(x) for x in input().split()]
    empresa = bool(_empresa)
    cidade1, cidade2 = cidades[id1], cidades[id2]
    cidade1.conexoes.append(Conexao(cidade2, empresa))
    cidade2.conexoes.append(Conexao(cidade1, empresa))

def pegar_maior_dist(origem: Cidade):
    maior_dist = 0
    def achar_maior_dist(origem: Cidade, id_ultima: int = 0, ultima_empresa: bool | None = None, dist: int = 1):
        nonlocal maior_dist
        maior_dist = max(maior_dist, dist)
        for conexao in origem.conexoes:
            cidade = conexao.destino
            if conexao.empresa == ultima_empresa: continue
            if cidade.id == id_ultima: continue
            achar_maior_dist(cidade, origem.id, conexao.empresa, dist + 1)
    
    achar_maior_dist(origem)
    return maior_dist

maior_dist = 1
for cidade in cidades:
    maior_dist = max(pegar_maior_dist(cidade), maior_dist)

print(maior_dist)