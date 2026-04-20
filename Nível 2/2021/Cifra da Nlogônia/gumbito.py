alfabeto = 'abcdefghijklmnopqrstuvxz'
vogais = set('aeiou')

palavra = input()

def vogal_mais_proxima(letra: str) -> str:
    pos_letra = alfabeto.index(letra)
    pos_vogal = 0

    for i in range(pos_letra - 1, -1, -1):
        if alfabeto[i] in vogais:
            pos_vogal = i
            break

    dist = pos_letra - pos_vogal
    for i in range(pos_letra + 1, pos_letra + dist):
        if alfabeto[i] in vogais:
            pos_vogal = i
            break
    
    return alfabeto[pos_vogal]
    
def consoante_seguinte(letra: str) -> str:
    pos_letra = alfabeto.index(letra)
    for i in range(pos_letra + 1, len(alfabeto)):
        if alfabeto[i] not in vogais:
            return alfabeto[i]
    return 'z'

cifrada = ''
for letra in palavra:
    cifrada += letra
    if letra in vogais: continue
    cifrada += vogal_mais_proxima(letra) + consoante_seguinte(letra)

print(cifrada)