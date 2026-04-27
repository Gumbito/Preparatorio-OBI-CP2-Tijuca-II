a, b, c = [int(input()) for _ in range(3)]

if   (b - a) < (c - b): print(1)
elif (b - a) > (c - b): print(-1)
else: print(0)

# questão pra ver se o candidato tá vivo