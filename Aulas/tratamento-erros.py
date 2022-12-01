# Tratando erros com Try e Except

letras = ['a', 'b', 'c']
try:
    print(letras[3])
except IndexError:
    print('An exception occurred')

try:
    x = int(input('Digite um numero'))
    print(x)
except ValueError:
    print('An exception occurred')


# Adicionando Else e Finnaly
try:
    x = int(input('Digite um numero'))
    print(x)
except ValueError:
    print('An exception occurred')
else:  # O else só será executado em caso de sucesso

    print("Codigo executado com sucesso!")

try:
    x = int(input('Digite um numero'))
    print(x)
except ValueError:
    print('An exception occurred')
finally:  # O finally será executado em caso de sucesso ou erro
    print("Codigo executado")
