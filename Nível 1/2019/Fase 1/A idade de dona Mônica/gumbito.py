idade_monica = int(input())
idades_filhos = [int(input()) for _ in range(2)]

idade_outro_filho = idade_monica - sum(idades_filhos)
idades_filhos.append(idade_outro_filho)
print(max(idades_filhos))