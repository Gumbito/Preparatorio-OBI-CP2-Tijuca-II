VALORES = {
    'A': 10,
    'J': 11,
    'Q': 12,
    'K': 13
}
BONUS_DOMINANTE = +4

CARTAS_POR_JOGADOR = 3

JOGADORES = ('Luana', 'Edu')

figura_tanto_faz, naipe_dominante = input()

pontos = [0] * len(JOGADORES)
for i in range(len(JOGADORES)):
    for _ in range(CARTAS_POR_JOGADOR):
        figura, naipe = input()
        valor_carta = VALORES[figura] + (BONUS_DOMINANTE if naipe == naipe_dominante else 0)
        pontos[i] += valor_carta

maior_pontuacao = max(pontos)
if pontos.count(maior_pontuacao) > 1:
    print('empate')
else:
    index_do_maioral = pontos.index(maior_pontuacao)
    print(JOGADORES[index_do_maioral])

# isso escala com a quantidade de jogadores, mas não muito bem,
# já que na verificação de ganhadores,
# a tuple de jogadores é percorrida 3 vezes.
# é possível diminuir isso pra 2 ou até 1
# sem falar que em algumas vezes percorrendo a tuple,
# o processo continua mesmo podendo parar antes de realmente percorrer tudo