qsecoes = int(input())
alturas_paredes = [int(input()) for _ in range(qsecoes)]

alturas_agua = [0] * qsecoes

# esquerda -> direita
maior = alturas_paredes[0]
for i in range(qsecoes):
    altura = alturas_paredes[i]
    maior = max(maior, altura)
    alturas_agua[i] = maior

# direita -> esquerda
maior = alturas_paredes[-1]
for i in reversed(range(qsecoes)):
    altura = alturas_paredes[i]
    maior = max(maior, altura)
    alturas_agua[i] = min(alturas_agua[i], maior)

# contando as seções cobertas por agua
qcobertas = 0
for altura_parede, altura_agua in zip(alturas_paredes, alturas_agua):
    if altura_agua > altura_parede:
        qcobertas += 1

print(qcobertas)

# python é muito lento pra OBI de 2016 pelo visto