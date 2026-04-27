qalunos = int(input())
alturas = [int(x) for x in input().split()]

alunos_invisiveis = 0
maior_altura = 0
for altura in reversed(alturas):
    if altura <= maior_altura:
        alunos_invisiveis += 1
    else:
        maior_altura = altura

print(alunos_invisiveis)