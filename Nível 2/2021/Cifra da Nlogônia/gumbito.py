alfabeto = 'abcdefghijklmnopqrstuvxz'
vogais = set('aeiou')

palavra = input()

def vogal_mais_proxima(letra: str) -> str:
    pos_letra = alfabeto.index(letra)
    pos_vogal = 0

    # procura a vogal mais próxima à esquerda
    for pos in reversed(range(pos_letra)):
        possivel_vogal = alfabeto[pos]
        if possivel_vogal in vogais:
            pos_vogal = pos
            break

    # distância da letra até a vogal mais próxima à esquerda
    dist = pos_letra - pos_vogal
    
    # procura a vogal mais próxima à direita andando menos que antes
    for pos in range(pos_letra + 1, min(pos_letra + dist, len(alfabeto))):
        # esse min limita a busca ao fim do alfabeto
        possivel_vogal = alfabeto[pos]
        if possivel_vogal in vogais:
            pos_vogal = pos
            break
    
    return alfabeto[pos_vogal]
    
def consoante_seguinte(letra: str) -> str:
    pos_letra = alfabeto.index(letra)
    for pos in range(pos_letra + 1, len(alfabeto)):
        possivel_consoante = alfabeto[pos]
        if possivel_consoante not in vogais:
            return possivel_consoante
    return 'z'


for letra in palavra:
    if letra in vogais:
        print(letra, end='')
        continue
    print(letra, end='')
    print(vogal_mais_proxima(letra), end='')
    print(consoante_seguinte(letra), end='')

# printando direto porque eu posso e é mais eficiente
# montar uma string somando caracteres é O(n^2)... assustador