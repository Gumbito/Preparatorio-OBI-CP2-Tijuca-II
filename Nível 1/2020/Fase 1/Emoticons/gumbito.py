# eu gosto de constantes, elas geralmente deixam o código mais entendível

EMOTICON_DIVERTIDO = ':-)'
EMOTICON_CHATEADO =  ':-('

OUTPUT_DIVERTIDO = 'divertido'
OUTPUT_NEUTRO = 'neutro'
OUTPUT_CHATEADO = 'chateado'

mensagem = input()

qdivertido = mensagem.count(EMOTICON_DIVERTIDO)
qchateado = mensagem.count(EMOTICON_CHATEADO)

if   qdivertido > qchateado: print(OUTPUT_DIVERTIDO)
elif qchateado > qdivertido: print(OUTPUT_CHATEADO)
else: print(OUTPUT_NEUTRO)