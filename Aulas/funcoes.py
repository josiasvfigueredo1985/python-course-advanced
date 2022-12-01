# Funções
# Exemplço de uma função básica
import math


def hello():
    print('Olá Mundo!')


hello()


def somar(n1, n2):
    result = n1+n2
    return print(result)


somar(2, 3)
# Função com parâmetros default
# funções devem receber o parâmetro non-fedault sempre no final
# Exemplo de erro quando adiciona o parâmetro default no início
# def boas_vindas_1(nome='usuário', quantidade):
#     print(f'Olá {nome}, temos {quantidade} laptops em estoque')


def boas_vindas(nome='usuário', quantidade=2):
    print(f'Olá {nome}, temos {quantidade} laptops em estoque')


boas_vindas('Josias')
boas_vindas('Josias', 8)
boas_vindas()


def cliente(nome):
    print(f'Olá {nome}!')  # simplesmente executa uma tarefa


def cliente2(nome):
    return f'Olá {nome}!'  # Return armazena valor variável


x = (cliente('Josias'))  # None
y = (cliente2('Josias'))

print(x)  # None
print(y)


# X Args - Para funções que pode recer um número desconheciudo de argumentos
def soma(*num):
    result = 0
    for n in num:
        result += n
    return result


print(soma(1, 2, 3, 4, 5))


def agencia(**carro):  # com ** é possível passar os parâmetros com valores direto na chamada do método, sendo armazenados num dicionário
    return carro


print(agencia(marca='Fiat', modelo='Uno Mille'))
print(agencia(marca='Fiat', ano=1995))
# O método retorna um dicionário, dessa forma é possível acessar os dados normalmente
print(agencia(marca='Fiat', modelo='Uno Mille',
      cor='Preto', placa='RD7NMF')['marca'])

# Módulos
# Exemplo de importação de um módulo -> math
print(math.factorial(4))
num = 4
r = 1
for n in range(1, 5):
    r *= n
print(r)
