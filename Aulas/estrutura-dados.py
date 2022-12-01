# Listas

from sys import getsizeof
from array import array

lista_sup = ['arroz', 'feijão', 'molho tomate', 'sal']
print(lista_sup)
print(lista_sup[0])
lista_sup[3] = 'Aji Sal'
print(lista_sup)
# Funções de uma lista
lista_sup.append('Carne')
print(lista_sup)
lista_sup.insert(0, 'macarrão')
print(lista_sup)
lista_sup.remove('feijão')  # Remove por nome do objeto
print(lista_sup)
lista_sup.pop(2)  # Remove por index do objeto
print(lista_sup)


# Concatenando listas
letras = ['a', 'b', 'c', 'd', 'e']
nums = [1, 2, 3, 4, 5]
print(letras+nums)  # concat com +
letras.extend(nums)
print(letras)  # concat com extend

# Lista dentro de outra lista
items = [['item1', 'item2'], ['item3', 'item4'], [1, 2, 3, 4], [True, False]]
print(items)
print(items[0])
print(items[0][1])
print(items[1][1])
print(items[2][1])
print(items[3][1])


# Extraindo variáveis de uma lista
prods = ['maçã', 'laranja', 'mamão', 'pera', 'graviola']
# padrão de extração
f1, f2, f3, f4, f5 = prods
print(f1, f2, f3, f4)
# extraindo sem saber o índice da lista
f1, f2, f3, *fx = prods
print(f1, f2, f3)
print(fx)  # a variável *fx retorna todos os items restantes


# Loop dentro de uma lista
lista = [1, 2, 3, 4]
for x in lista:
    print(f'O valor final é {x}')

# Verificando itens dentrro de uma lista
cores = ['amarelo', 'azul', 'verde', 'vermelho', 'laranja', 'roxo', 'preto']
cor = input('Digite a cor desejada: ').lower()
while cor != 'fim':
    if cor in cores:
        print(f'A cor {cor} está em estoque')
        break
    else:
        print(f'A cor {cor} não está em estoque')
        cor = input('Digite a cor desejada: ').lower()


# Juntando duas listas com ZIP
mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
       'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
num_mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
ano = list(zip(mes, num_mes))
print(ano)
i = 0
for m in ano:
    print(f'Mês {m[i+1]} - {m[i].capitalize()}')
    i += i


# Input em uma lista
print('Entre com os dados obrigatório: nome, idade e cidade atual')
dados_user = input('Digite os dados separados por vírgula\n')
dados = dados_user.split(',')
print(dados)
for d in dados:
    print(d.strip())

# Tuples
cores_list = ['azul', 'amarelo', 'branco', 'azul', 'laranja', 'vermelho']
cores_tuple = ('azul', 'amarelo', 'branco', 'azul', 'laranja', 'vermelho')
print(cores_list)  # Listas são mutáveis
# Tuplas são imutáveis e possuem melhor performance que uma lista
print(cores_tuple)


# Arrays
letras = ['a', 'b', 'c', 'd']
numi = [1, 2, 3, 4]
numf = [1.0, 2.0, 3.0, 4.0]
ar1 = array('u', letras)
ar2 = array('i', numi)
ar3 = array('f', numf)
print(ar1, ar2, ar3)
for a in ar1:
    print(a)
for a in ar2:
    print(a)
for a in ar3:
    print(a)


# Sets
# Operadores
num1 = [1, 2, 3, 4, 5, 6]
num2 = [5, 6, 7, 8, 9, 0]
n1 = set(num1)
n2 = set(num2)
print(f'Lista 1: \n{n1} \nLista 2: \n{n2}')
print('# Union - Retira os repetidos')
print(n1 | n2)
print('# Difference - mostra os valores diferentes que não ocorrem na outra lista')
print(n1 - n2)
print(' # Simetric Difference - Mostra os valores únicos das 2 listas')
print(n1 ^ n2)
print('# And - Mostra somente os valores duplicados nas duas listas')
print(n1 & n2)
print(n1[0])  # Após usar o set não é possível usaro index de uma lista

# Set - Métodos Operadores
s1 = {'a', 'b', 'c'}
s2 = {'a', 'd', 'e'}
s3 = {'c', 'd', 'f'}
s4 = s1.union(s2)
print(s4)
s5 = s1.difference(s3)
print(s5)
s6 = s1.intersection(s2)
print(s6)
s7 = s1.symmetric_difference(s3)
print(s7)


# Funções em Sets
s1 = {1, 2, 3, 4}
print(s1)
s1.add(4)  # Não permite duplicados
print(s1)
s1.add(5)  # Permite adicionar novos items
print(s1)
s1.update([6, 7, 8, 9])
# Gera erro se item não existir na lista - ambos deletam um item da lista
s1.remove(10)
print(s1)
s1.discard(10)  # Não gera erro se item não existir na lista
print(s1)


# Dicionário

aluno = {'nome': 'Josias', 'nota': 8.0}
print(aluno)
print(aluno['nome'])
nota = aluno['nota']
status = ''
if nota <= 10:
    # Se a chave não existir ele irá acrescentar ao dicionário, se existir ele irá atualizar o valor da chave
    aluno['aprovado'] = False
    status = 'reprovado'
else:
    aluno['aprovado'] = False
    status = 'aprovado'
nome = str(aluno['nome'])
print(aluno)
print(f'O aluno {nome} está {status}')
# O update pode criar e atualizar mais de uma chave/valor ao mesmo tempo
aluno.update({'Turma': 'B', 'Turno': 'Manhã', 'Série': '7'})
print(aluno)
# não retorna erro (retorna None ou mensagem configurada)
print(aluno.get('idade', 'Dado inexistente'))
# se o dado exitir a mensagem configurada é ignorada e o dado é retornado
print(aluno.get('Turno', 'Dado inexistente'))
del aluno['Série']
print(aluno)
# print(aluno['idade'])  # retorna um erro


# Loops num dicionário
aluno = {'nome': 'Josias', 'nota': 8.0}
print('Keys:')
for x in aluno:  # imprime somente as keys
    print(x)
print('\nKeys:')
for x in aluno.keys():  # imprime somente as keys
    print(x)
print('\nValues:')
for x in aluno.values():  # imprime somente os values
    print(x)
print('\nItems:')
for x in aluno.items():  # imprime somente os values
    print(x)
print('\nItems formatado:')
for key, value in aluno.items():  # imprime somente os values
    print(key, value)

produto = {
    'marca': 'Sony',
    'modelo': 'PS5',
    'quantidade': 5,
    'compatibilidade': ['ps1', 'ps2', 'ps3', 'ps4', 'cd', 'dvd', 'cdrom', 'dvdrom', 'bluray']
}
print(produto)  # retorna o dicionário completo
print(produto.items())  # retorna o dicionáro e seus items
print(produto.keys())  # retorna as chaves do dicionário
print(produto.values())  # retorna somente os valoes de cada chave
# retorna a lista de items dentro do dicionário
print(produto['compatibilidade'])
# retorna o item dentro do index da lista dentro do dicionário
print(produto['compatibilidade'][0])


# Lambda functions
def somar(x):
    return lambda x: str(x) + ' A'


print(somar(2))

# Por boa prática, aconselha-se deixar a função lamnda dentro de uma função
# somar10 = lambda x: x+10


def somar10(x):
    return lambda x: x+10


print(somar10(2))

# Map function
lista = [1, 2, 3, 4]


def mult(x):
    return x*2


# Map com funçãp
lista2 = map(mult, lista)
print(list(lista2))
# map com lambda
lista2 = map(lambda x: x*2, lista)
print(list(lista2))
# print demap com lambda
print(list(map(lambda x: x*2, lista)))

# Filter
valores = [10, 20, 33, 45, 67]


def remover20(x):
    return x > 20


# retorna somente os valores maiores que 20 usando filter + função
print(list(filter(remover20, valores)))
# retorna somente os valores maiores que 20 usando filter + lambda
print(list(filter(lambda x: x > 20, valores)))


# List Comprehension com Strings

fruits = ['apple', 'banana', 'cherry', 'abacaxi', 'abacate']

# Maneira tradicional de criar uma segunda lista somente com  itens contendo a letra 'b'
fruits2 = []
for x in fruits:
    if 'b' in x:
        fruits2.append(x)

# Usando o list Comprehension - Resolve o mesmo problema com apenas 1 linha de código
fruits2 = [f for f in fruits if 'b' in f]
print(fruits2)

# List comprehension com números
nums2 = [x*10 for x in range(6)]
print(nums2)

# List comprehension com números
numers = [12332, 34433, 5654, 66, 4454]
nu2 = [f for f in numers if '4' in str(f)]
print(nu2)


# Generator Expression - Utiliza menos memória na geração de listas
numeros = [x*10 for x in range(1000)]
print(numeros)
print(type(numeros))
print(getsizeof(numeros))
# Diferente da lista, utiliza parênteses
numeros = (x*10 for x in range(1000))
print(list(numeros))
print(type(numeros))
print(getsizeof(numeros))
