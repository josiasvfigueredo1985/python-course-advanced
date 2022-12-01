# Criando classes e construtores
class Funcionarios:
    def __init__(self, nome, sobrenome, nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nascimento = nascimento


# Usando o construtor, é possível adicionar quantos objetos quiser sem precisar declarar todos novamente
# Criar o objeto para o usuario 1
usuario1 = Funcionarios('Dimitry', 'Slanevsky', '19/04/78')
# Criar o objeto para o usuario 2
usuario2 = Funcionarios('Maria', 'Carolitta', '10/08/1908')


# print do dado do objeto
print(usuario1.nome)
print(usuario1.sobrenome)
print(usuario1.nascimento)
# print do dado do objeto
print(usuario2.nome)
print(usuario2.sobrenome)
print(usuario2.nascimento)
