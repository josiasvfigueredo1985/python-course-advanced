# List Comprehension com Strings

fruits = ['apple', 'banana', 'cherry', 'abacaxi', 'abacate']

# Maneira tradicional de criar uma segunda lista somente com  itens contendo a letra 'b'
# fruits2 = []
# for x in fruits:
#     if 'b' in x:
#         fruits2.append(x)

# Usando o list Comprehension - Resolve o mesmo problema com apenas 1 linha de código
fruits2 = [f for f in fruits if 'b' in f]
print(fruits2)
