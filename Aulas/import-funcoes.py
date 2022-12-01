# Criando módulos
# Import mais indicado
from funcoes import find_index
from funcoes_import import multi, somar
# Imports - este tipo de imporetação pode pesar muito o processamento quando um módulo possui muitas funções, pois todas serão carregadas
# Import com atribuição à um objeto
import funcoes_import as func
# Import sem atribuição
import funcoes_import

# Import não indicado sem objeto atribuído
funcoes_import.somar()
funcoes_import.multi()

# Import não indicado com objeto 'func' atribuído
func.somar()
func.multi()

# O import from permite acessar a função diretamente, sem precisar atribuir nenhum objeto ao módulo
somar()
multi()

# Mais exemplos de Import de funções

list_items = ['a', 'b', 'c', 'd', 'e', 'f']
var1 = find_index(list_items, 'a')
print(var1)
