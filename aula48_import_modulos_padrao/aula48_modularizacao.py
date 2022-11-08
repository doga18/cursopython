# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

import aula48_modularizacao_module

from aula48_modularizacao_module import variavel_modulo, soma

print('Este módulo se chama', __name__)

print(aula48_modularizacao_module.variavel_modulo)

print(variavel_modulo)

print(soma(1, 2))

print(aula48_modularizacao_module.soma(1, 4))