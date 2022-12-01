# Ponto do Steak - If, Elif e Else
'''
< 48 - A carne deve assar mais um pouco
> = 48 and < 54 - Selada
> = 54 and < 60 - Ao ponto pra mal
> = 60 and < 65 - Ao ponto
> = 65 and < 71 - Ao ponto pra bem
> 71 - Bem passada

'''


def ponto_steak_1(graus):
    ponto = ['A carne deve assar mais um pouco!',
             'A carne está selada!',
             'A carne está no ponto pra mal passada!',
             'A carne está no ponto!',
             'A carne está no ponto pra bem passada!',
             'A carne está bem passada!',
             'A carne queimou!']
    i = 0
    # if graus in range(0, 48) Alternativa ao operador múltiplo
    if graus < 48:
        i = 0
    elif 48 <= graus < 54:
        i = 1
    elif 54 <= graus < 60:
        i = 2
    elif 60 <= graus < 65:
        i = 3
    elif 65 <= graus < 71:
        i = 4
    elif 71 <= graus <= 80:
        i = 5
    else:
        i = 6
    return print(ponto[i])


temperatura_carne = int(input('Qual a temperatura da carne?\n'))
ponto_steak_1(temperatura_carne)


def ponto_steak_2(graus):
    ponto = ['A carne deve assar mais um pouco!',
             'A carne está selada!',
             'A carne está no ponto pra mal passada!',
             'A carne está no ponto!',
             'A carne está no ponto pra bem passada!',
             'A carne está bem passada!',
             'A carne queimou!']
    i = 0
    # Alternativa ao operador múltiplo
    if graus in range(0, 48):
        i = 0
    elif graus in range(48, 54):
        i = 1
    elif graus in range(54, 60):
        i = 2
    elif graus in range(60, 65):
        i = 3
    elif graus in range(65, 71):
        i = 4
    elif graus in range(71, 80):
        i = 5
    else:
        i = 6
    return print(ponto[i])


temperatura_carne = int(input('Qual a temperatura da carne?\n'))
ponto_steak_2(temperatura_carne)
