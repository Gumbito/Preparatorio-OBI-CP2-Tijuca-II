qnumeros = int(input())

numeros: list[int] = []
for _ in range(qnumeros):
    numero = int(input())
    if (numero == 0) and (len(numeros) > 0): numeros.pop()
    else: numeros.append(numero)

print(sum(numeros))