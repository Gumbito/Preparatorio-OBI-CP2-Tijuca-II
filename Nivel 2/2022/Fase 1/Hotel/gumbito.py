DIAS_NO_MES = 31
diaria_inicial, aumento, chegada = [int(input()) for _ in range(3)]
diaria = diaria_inicial + (min(15, chegada) - 1) * aumento
qdias = (DIAS_NO_MES - chegada) + 1
total = diaria * qdias
print(total)