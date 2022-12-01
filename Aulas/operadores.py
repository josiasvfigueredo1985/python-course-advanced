
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

print('True bloco\nNumber')

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

print('False bloco:\nNumber')

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
