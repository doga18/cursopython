import importlib # Isso será sempre de utilidade de recarregar o módulo mais de uma vez, o módulo IMPORT sempre será carregado somente uma vez.
import aula48_modularizacao_module

print(aula48_modularizacao_module.variavel_modulo)

for i in range(10):
    importlib.reload(aula48_modularizacao_module)
    print(i)

print('Fim')

