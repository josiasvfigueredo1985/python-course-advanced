# Só é possível chamar um package se o mmesmo estiver dentro do package do projeto ou a classe estiver na raíz do projeto
# Exemplo Main/Projeto/Package -> Funciona
# Exemplo Main/Package/Projeto -> Não funciona

from package.cadastro import cadastra
from package.calculo import calcula

cadastra()
calcula()
