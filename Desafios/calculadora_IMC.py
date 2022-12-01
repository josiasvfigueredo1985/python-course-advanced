'''
Calculadora IMC
Altura em cm:
Peso em kg
'''
# Fórmula IMC = kg / (altura*altura)


def calculadora_IMC():
    altura = float(input('Digite sua altura em cm:\n'))
    kg = float(input('Digite o seu peso:\n'))
    tabela = ['Magreza', 'Normal', 'Sobrepeso', 'Obesidade', 'Obesidade Grave']
    imc = kg / (altura/100)**2
    i = 0
    if imc < 18.5:
        i = 0
    elif 18.5 <= imc < 24.9:
        i = 1
    elif 25.0 <= imc < 29.9:
        i = 2
    elif 30.0 <= imc < 39.9:
        i = 3
    elif imc > 40.0:
        i = 4
    print(f'O seu imc é de {round(imc,2)} e sua condição é {tabela[i]}')


calculadora_IMC()
