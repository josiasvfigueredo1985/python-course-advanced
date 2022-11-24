# Comentários

# Single line

'''
Múltiplas linhas
ou
bloco
de comentário
'''

# Data types/ Variáveis
'''
string = 'string'
inteiro = 1
double = 1.5
booleano = True
print(type(string))  # str
print(type(inteiro))  # integer
print(type(double))  # float
print(type(booleano))  # bool
'''

'''
# Modificando tipos de dados

x = str(3)
y = int(4)
z = float(5)
print(x)
print(y)
print(z)


# Pratica com string e integers
nome = 'Josias'
idade = 37
cidade = 'São Paulo'
print('Olá, eu sou ' + nome + ', tenho ' + str(idade) + ' e moro em ' + cidade)
'''

'''
# Adicionando input

nome = input('Olá, qual o seu nome?\n')
idade = input('Qual o sua idade?\n')
cidade = input('Qual sua cidade?\n')


print('Muito prazer, ' + nome + '! \nSua idade é ' +
      idade + ' e você mora em ' + cidade)

# Calculando idade com input

ano = input('Olá, qual o ano do seu nascimento?\n')
ano_atual = input('Qual o ano atual?\n')
print('A sua idade é: ' + str(int(ano_atual)-int(ano)))

'''

'''
# Slice
fruta = 'Abacate'
# Index
print(fruta[2])
print(fruta[2:6])
print(fruta[-1])

valor = 10.25
valor = str(valor)
# Somando valor inteiro com os centavos
real = valor[:2]
centavos = valor[3:]
print('Valores de real: '+real)
print('Valores de centavos: '+centavos)

# Conversão para integer
real = int(real)
centavos = int(centavos)
print('Soma dos valores: '+str(real+centavos))

'''

'''
# Formated Strings
nome = 'Josias'
sobrenome = 'Valentim'
profissao = 'QA'
texto = 'O ' + nome + ' '+sobrenome + \
    ' é um excelente ' + profissao  # string comum
print(texto)

texto2 = f'O {nome} {sobrenome} é um excelente {profissao}'  # String formatada
print(texto2)
'''

'''
# Métodos para string

mensagem = 'eu adoro comida caseira!'

print(mensagem.lower())
print(mensagem.upper())
print(mensagem.capitalize())
print(mensagem.find('adoro'))
print(mensagem.replace('a', 'e'))
print(mensagem.replace('caseira', 'de fogão de lenha'))
print('   eu adoro comida caseira!   '.strip())
'''


'''
# Operações matemática

# Ordem dos cálculos
# 1 - Parênteses
print('Prioridade padrão das operações matemáticas')
print('1 - Parênteses: ', (2+2)*2)  # 8
# 2 - Exponencial
print('2 - Exponencial: ', 2**4+1)  # 17
# 3 - Multiplicação
print('3 - Multiplicação: ', 4+4*2)  # 12
# 4 - Divisão
print('4 - Divisão: ', 4+2/2)  # 5
# 5 - Adição e Subtração
print('5 - Adição/Subtração: ', 5+10-5)  # 4

print('-'*150)
# 1 - Parênteses
print('Sem Prioridade padrão das operações matemáticas')
print('1 - Parênteses: ', 2+2*2)  # 6
# 2 - Exponencial
print('2 - Exponencial: ', 2**(4+1))  # 32
# 3 - Multiplicação
print('3 - Multiplicação: ', (4+4)*2)  # 16
# 4 - Divisão
print('4 - Divisão: ', (4+2)/2)  # 3

'''

'''
# Operadores de comparação
# == Equal
# != Not equal
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to

x = 10
y = 20
a = 'apple'
b = 'banana'

print('True block\nNumber')

print(x == x)
print(x != y)
print(y > x)
print(x < y)
print(y >= x)
print(x <= y)

print('String')

print(a == a)
print(a != b)
print(b > a)
print(a < b)
print(b >= a)
print(a <= b)

print('-'*140)

print('False block:\nNumber')

print(x == y)
print(x != x)
print(x > y)
print(y < x)
print(x >= y)
print(y <= x)

print('\n')

print('String')

print(a == b)
print(a != a)
print(a > b)
print(b < a)
print(a >= b)
print(b <= a)

'''

'''
# Operadores de atribuição
x = 10
x *= 5
print(f'Multiplicação:  {x}')
x = 10
x /= 2
print(f'Divisão:  {x}')
x = 10
x += 5
print(f'Adição:  {x}')
x = 10
x -= 5
print(f'Subtração:  {x}')
x = 10
x %= 4
print(f'Resto:  {x}')

'''

'''
# Condicionais if e else
velocidade = 40
if velocidade > 110:
    print('Acima da velocidade permitida')
elif velocidade < 60:
    print('Favor dirigir acima de 80km/h')
else:
    print('Velocidade ok')

'''

'''
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
'''

'''
# Operador ternário
idade = 16
resultado = 'Voto permitido' if idade >= 16 else 'Voto não permitido'
print(resultado)
'''


'''
# Mutltiplos operadores de comparfação

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
'''

'''
# For loops - Nubers

for x in range(6):  # 0 to 5
    print(x)
print('---'*50)
for x in range(2, 6):  # 2 to 5
    print(x)
print('---'*50)
for x in range(2, 30, 3):  # 2 to 30 incrementing 3 for each loop
    print(x)
'''


'''
# For loops strings
palavra = 'Microsoft'

for letra in palavra:
    print(letra)
'''

'''
# Foor loop if/else

compra_confirmada = True
dados = "Compra confirmada!"

for x in range(3):
    if compra_confirmada:
        print(dados)
        break
else:
    print('Compra não confirmada!')
'''

'''
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
        print(simbolo,end='')
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

'''
