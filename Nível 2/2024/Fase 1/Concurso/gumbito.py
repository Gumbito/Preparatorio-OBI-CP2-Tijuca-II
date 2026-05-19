qparticipantes, min_aprovados = [int(x) for x in input().split()]
notas = [int(x) for x in input().split()]

notas.sort(reverse=True)
nota_corte = notas[min_aprovados - 1]

print(nota_corte)