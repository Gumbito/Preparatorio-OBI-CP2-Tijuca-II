# NÃO É A MESMA QUESTÃO QUE "Café com Leite" DO MESMO ANO E MESMA FASE
# ^ acho que isso devia estar numa nota dentro da pasta da questão,
# não na minha solução em específico
# 
# eu coloquei esse aviso na "Café com Leite" também...hm
# tanto faz, vou deixar como tá mesmo

SIM = 'S'
NAO = 'N'

min_leite, max_leite = [int(input()) for _ in range(2)]
capacidade_xicara = int(input())
cafe_por_dose = int(input())

min_cafe = capacidade_xicara - max_leite
max_cafe = capacidade_xicara - min_leite

def qdoses_valida(qdoses: int) -> bool:
    qcafe = qdoses * cafe_por_dose
    return min_cafe <= qcafe <= max_cafe

# primeira quantidade de doses que pode dar certo:
qdoses = min_cafe // cafe_por_dose
if qdoses_valida(qdoses):
    print(SIM)
    exit()

# segunda quantidade de doses que pode dar certo (se a primeira não deu)
qdoses += 1
if qdoses_valida(qdoses):
    print(SIM)
    exit()

# se nem a segunda funcionou, quer dizer que ela ultrapassou a quantidade
# máxima de café permitida pelas regras e não é possível satisfazer o cliente

print(NAO)