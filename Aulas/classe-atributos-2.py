# Criando classes
class Funcionarios:
    pass


# Criar o objeto para o usuario 1
usuario1 = Funcionarios()
# Criar o objeto para o usuario 2
usuario2 = Funcionarios()

# Por atribuição é possível adicionar e manipular objetos à uma classe
# criar parametros do usuario 1 por meio de atribuição
usuario1.nome = 'Dimitry'
usuario1.sobrenome = 'Novsky'
usuario1.nascimento = '19/05/1988'

# criar parametros do usuario 2 por meio de atribuição
usuario2.nome = 'Ophelia'
usuario2.sobrenome = 'Matruscci'
usuario2.nascimento = '19/05/1359'

# print do dado do objeto usuário 1
print(usuario1.nome)
print(usuario1.sobrenome)
print(usuario1.nascimento)
# print do dado do objeto usuário 2
print(usuario2.nome)
print(usuario2.sobrenome)
print(usuario2.nascimento)
