'''
# Lambda functions

def somar(x):
    def func2(x): return str(x) + ' A'
    return func2(x)


print(somar(2))


def somar10(x): return x+10


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
'''

# Filter
valores = [10, 20, 33, 45, 67]


def remover20(x):
    return x > 20


# retorna somente os valores maiores que 20 usando filter + função
print(list(filter(remover20, valores)))
# retorna somente os valores maiores que 20 usando filter + lambda
print(list(filter(lambda x: x > 20, valores)))
