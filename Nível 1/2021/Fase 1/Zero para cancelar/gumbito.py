qnumeros = int(input())

numeros: list[int] = []
for _ in range(qnumeros):
    numero = int(input())
    if numero != 0:
        numeros.append(numero)
    elif numeros:
        numeros.pop()

print(sum(numeros))