qgrandes, qpequenas = [int(input()) for _ in range(2)]

qfatias = (8 * qgrandes) + (4 * qpequenas)

max_convidados = qfatias - 2 # (-2 já que 2 fatias são para as anfitriãs)
print(max_convidados)