from funcoes import calcula_rendimento
'''
Função pra calcular quantidade de tinta necessária pra pintar uma parede
Argumentos: rendiomento, altura e largura
Mensagem: 'Você necessita de x latas de tinta
'''


def rendimento_tinta():
    rendimento = float(input('Digite o rendimento da lata de tinta:\n'))
    altura = float(input('Digite a altura da parede:\n'))
    largura = float(input('Digite a largura da parede:\n'))
    calcula_rendimento(rendimento, altura, largura)


rendimento_tinta()
