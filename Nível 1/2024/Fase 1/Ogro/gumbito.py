esquerda, direita = [int(input()) for _ in range(2)]

resultado: int | None = None
if esquerda > direita:
    resultado = esquerda + direita
else:
    resultado = 2 * (direita - esquerda)

print(resultado)