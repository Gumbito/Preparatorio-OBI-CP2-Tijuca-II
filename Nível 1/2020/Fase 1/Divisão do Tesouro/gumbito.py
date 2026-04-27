qmoedas = int(input())
qmarinheiros = int(input())

#region explicação da fórmula
# quantidade total de moedas = t
# quantidade de marinheiros = q
# quantidade de moedas para cada marinheiro = m
# quantidade de moedas para o capitão = c
# a questão diz que o capitão recebe o dobro de moedas que um marinheiro recebe
# portanto c = 2m, logo m = c/2

# queremos descobrir c em termos de t, q e/ou m
# continhas:
# t = c + qm
# => t = 2m + qm .....# (substituí c por 2m)
# => t = m(2 + q) ....# (coloquei m em evidência)
# => t/(2 + q) = m ...# (dividi por (2 + q) nos dois lados para isolar m)
# => m = t/(2 + q) ...# (só inverti a ordem pra melhor vizualização)
# => c/2 = t/(2 + q) .# (substituí m por c/2)
# => c = 2(t/(2 + q)) # (multipliequei por 2 nos dois lados para isolar c)

# perfeito, temos c em termos de variáveis que somos dados, agora é só aplicar:
#endregion

qmoedas_capitao = int(2 * (qmoedas/(2 + qmarinheiros)))

#region explicação da conversão para int
# quando acontece uma divisão de um inteiro por outro,
# mesmo que o resultado seja inteiro,
# é retornado um float.
#
# a conversão é feita para inteiro por conta de formatação,
# já que floats, mesmo tendo apenas partes inteiras,
# são formatados com no mínimo uma casa decimal (e não queremos isso).
# caso não houvesse a conversão, e o resultado valesse, por exemplo, 34,
# o resultado seria printado como "34.0"
#
# quando um float é convertido para inteiro, ele perde sua parte decimal,
# mas nesse caso parte não-inteira não é "perdida", já que ela não existe,
# pois a questão garante que o resultado será um número inteiro.
#endregion

print(qmoedas_capitao)

# "i aint reading allat"