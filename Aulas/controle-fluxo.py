# Condicionais if e else
velocidade = 40
if velocidade > 110:
    print('Acima da velocidade permitida')
elif velocidade < 60:
    print('Favor dirigir acima de 80km/h')
else:
    print('Velocidade ok')

# Operadores lógicos
renda = True
nome_limpo = True
if renda and nome_limpo:
    print('Financiamento Aprovado!')
else:
    print('Financimento Negado!')

renda = True
nome_limpo = False
if renda and nome_limpo:
    print('Financiamento Aprovado!')
else:
    print('Financimento Negado!')

renda = True
nome_limpo = False
if renda or nome_limpo:
    print('Financiamento Aprovado!')
else:
    print('Financimento Negado!')

# Operador ternário
idade = 16
resultado = 'Voto permitido' if idade >= 16 else 'Voto não permitido'
print(resultado)

# Mutltiplos operadores de comparação
# Maneira normal
valor = 20
print('Sem múltiplo operador')
if valor >= 20 and valor < 40:
    print('Produto aceito')
else:
    print('Produto não aceito')

# Com múltiplos operadores
valor = 20
print('Com mútiplos operadores')
# 20<= <-valor-> <40
if 20 <= valor < 40:
    print('Produto aceito')
else:
    print('Produto não aceito')

# For loops - Nubers
for x in range(6):  # 0 to 5
    print(x)
print('---'*50)
for x in range(2, 6):  # 2 to 5
    print(x)
print('---'*50)
for x in range(2, 30, 3):  # 2 pra 30 incrementando 3 pra cada loop
    print(x)


# For loops strings
palavra = 'Microsoft'

for letra in palavra:
    print(letra)


# Foor loop if/else

compra_confirmada = True
dados = "Compra confirmada!"

for x in range(3):
    if compra_confirmada:
        print(dados)
        break
else:
    print('Compra não confirmada!')


# Nested loop

adj = ['red', 'big', 'tasty']
fruits = ['apple', 'banana', 'cherry']
for x in adj:
    for y in fruits:
        print(x, y)

# Adiciona espaço entra as letras
palavra = 'FANTASTICO'
for espaco in palavra:
    print(f'{espaco}', end=' ')

# Criar um quadrado com o for loop
linha = 60
simbolo = '*'

for l in range(int(linha/4)):
    for c in range(linha):
        print(simbolo, end='')
    print()


symbol = '*'
width = 100
heigth = 5

l1 = symbol * width
print(l1)
for i in range(heigth - 2):
    l2 = symbol + (' ' * (width-2)*len(symbol)) + symbol
    print(l2)
print(l1)


line = 20
symbol = '*'
l3 = symbol * line
print('Square')
print(l3)
for i in range(line - int(line*0.7)):
    l2 = symbol + (' ' * (line-2)*len(symbol)) + symbol
    print(l2)
print(l3)
print(int(line*0.7))


# While loop - 1
valor = 100
dia = 1
while valor > 20:
    print(f'No dia {dia} o produto será vendido no {valor}')
    dia += 1
    valor -= 5


valor = 50
while valor > 20:
    valor = (valor*0.20) + valor
    print(f'O valor final é de R$ {valor}')
    break
