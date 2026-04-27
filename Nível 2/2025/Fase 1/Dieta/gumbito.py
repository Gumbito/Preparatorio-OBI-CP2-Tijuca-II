qrefeicoes, limite_cals = [int(x) for x in input().split()]

cals_consumidas = 0
for _ in range(qrefeicoes):
    qproteinas, qgorduras, qcarboidratos = [int(x) for x in input().split()]
    cals_consumidas += 4 * qproteinas
    cals_consumidas += 9 * qgorduras
    cals_consumidas += 4 * qcarboidratos

calorias_que_o_garfield_ainda_pode_consumir = limite_cals - cals_consumidas
print(calorias_que_o_garfield_ainda_pode_consumir)

# eu ia colocar o nome da váriável de
# "a_quantidade_maxima_de_calorias_que_o_garfield_ainda_pode_consumir_sem_exceder_o_limite_m",
# mas achei um pouco longo demais