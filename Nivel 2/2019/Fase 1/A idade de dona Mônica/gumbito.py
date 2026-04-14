idade_monica = int(input())
idades_filhos = [int(input()) for _ in range(2)]

idades_filhos.append(idade_monica - sum(idades_filhos))
print(max(idades_filhos))