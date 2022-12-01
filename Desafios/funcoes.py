def calcula_metro_quadrado(altura, largura):
    return float(altura * largura)


def calcula_tinta(rendimento, metro_quadrado):
    tinta = metro_quadrado / rendimento
    return float(tinta)


def calcula_rendimento(rendimento: float, altura: float, largura: float):
    mt = calcula_metro_quadrado(altura, largura)
    tinta = calcula_tinta(rendimento, mt)
    lt = ''
    if tinta > 1:
        lt = 'latas'
    else:
        lt = 'lata'
    return print(f'Você necessita de {tinta} {lt} de tinta')


