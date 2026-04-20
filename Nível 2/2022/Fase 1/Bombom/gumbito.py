VALORES = {
    'A': 10,
    'J': 11,
    'Q': 12,
    'K': 13
}
BONUS_DOMINANTE = +4

QJOGADORES = 2
CARTAS_POR_JOGADOR = 3
NOMES = ['Luana', 'Edu']

naipe_dominante = input()[1]

pontos = [0] * QJOGADORES
for i in range(QJOGADORES):
    for _ in range(CARTAS_POR_JOGADOR):
        figura, naipe = input()
        valor_carta = VALORES[figura] + (BONUS_DOMINANTE if naipe == naipe_dominante else 0)
        pontos[i] += valor_carta

maior_pontuacao = max(pontos)
if pontos.count(maior_pontuacao) > 1: print('empate')
else: print(NOMES[pontos.index(maior_pontuacao)])

# percorrendo a lista 3 vezes por que eu quero e posso :)