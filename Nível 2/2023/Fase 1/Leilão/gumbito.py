qlances = int(input())

nome_ganhador = ''
valor_ganhador = 0

for lance in range(qlances):
    nome = input()
    valor = int(input())
    if valor > valor_ganhador:
        nome_ganhador = nome
        valor_ganhador = valor

print(nome_ganhador)
print(valor_ganhador)