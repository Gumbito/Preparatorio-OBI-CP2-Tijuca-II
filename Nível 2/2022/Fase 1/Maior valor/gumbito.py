inicio, fim, soma_alvo = [int(input()) for _ in range(3)]

for num in range(fim, inicio - 1, -1):
    soma = sum([int(d) for d in str(num)])
    if soma == soma_alvo:
        print(num)
        exit()

print(-1)

# deve ter um jeito de fazer isso sem percorrer número por número
# hmm...
# 
# é bem possível que tenha mesmo