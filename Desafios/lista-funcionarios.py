'''
Criar um programa que gera  listas conforme a necessidade abaixo:
Lista 1 = Funcionários que tem carro e trabalham a noite
Lista 2 = Funcionários que tem carro e trabalham de dia
Lista 3 = Funcionários que não tem carro
'''


def lista_funcionarios():
    funcionarios = ['Ana', 'Marcos', 'Alice',
                    'Pedro', 'Sophia', 'Bruno', 'Melissa']
    turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
    turno_noite = ['Pedro', 'Sophia', 'Bruno']
    tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

    f = set(funcionarios)
    d = set(turno_dia)
    n = set(turno_noite)
    c = set(tem_carro)
    print('# Usando operadores')
    print('# Lista 1 = Funcionários que tem carro e trabalham a noite')
    print(c & n)
    print('# Lista 2 = Funcionários que tem carro e trabalham de dia')
    print(c & d)
    print('# Lista 3 = Funcionários que não tem carro')
    print(f - c)
    print('# Usando Intersection')
    lista1 = set(c).intersection(n)
    lista2 = set(c).intersection(d)
    lista3 = set(f).difference(c)
    print(f'{lista1}\n{lista2}\n{lista3}')


lista_funcionarios()
