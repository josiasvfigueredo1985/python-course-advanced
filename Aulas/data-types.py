# Data types/ Variáveis
string = 'string'
inteiro = 1
double = 1.5
booleano = True
print(type(string))  # str
print(type(inteiro))  # integer
print(type(double))  # float
print(type(booleano))  # bool

# Modificando tipos de dados
x = str(3)
y = int(4)
z = float(5)
print(x)
print(y)
print(z)

# Prática com string e integers
nome = 'Josias'
idade = 37
cidade = 'São Paulo'
print('Olá, eu sou ' + nome + ', tenho ' + str(idade) + ' e moro em ' + cidade)

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


# Slice - String
fruta = 'Abacate'
# Index
print(fruta[2])
print(fruta[2:6])
print(fruta[-1])
# Slice - Float
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

# Formated Strings
nome = 'Josias'
sobrenome = 'Valentim'
profissao = 'QA'
texto = 'O ' + nome + ' '+sobrenome + \
    ' é um excelente ' + profissao  # string comum
print(texto)
texto2 = f'O {nome} {sobrenome} é um excelente {profissao}'  # String formatada
print(texto2)

# Métodos para string
mensagem = 'eu adoro comida caseira!'
print(mensagem.lower())
print(mensagem.upper())
print(mensagem.capitalize())
print(mensagem.find('adoro'))
print(mensagem.replace('a', 'e'))
print(mensagem.replace('caseira', 'de fogão de lenha'))
print('   eu adoro comida caseira!   '.strip())
