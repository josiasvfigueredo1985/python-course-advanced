# Criando classes e construtores + funções
from datetime import datetime
import re


class Funcionarios:
    def __init__(self, nome, sobrenome, nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nascimento = nascimento

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    def calcula_idade(self):
        ano_atual = datetime.now().year
        return ano_atual - int(re.split('/', self.nascimento)[2])


# Usando o construtor, é possível adicionar quantos objetos quiser sem precisar declarar todos novamente
# Criar o objeto para o usuario 1
usuario1 = Funcionarios('Dimitry', 'Slanevsky', '19/04/1983')
# Criar o objeto para o usuario 2
usuario2 = Funcionarios('Maria', 'Carolitta', '10/08/1908')

# Usando a função da classe - Opção 1
print(usuario1.nome_completo())
print(usuario2.nome_completo())

# Chamando a função a partir da classe - Opção 2 - Melhor legibilidade
print(Funcionarios.nome_completo(usuario1))
print(Funcionarios.nome_completo(usuario2))
print(Funcionarios.calcula_idade(usuario1))
