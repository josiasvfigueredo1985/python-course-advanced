'''
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
'''
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
