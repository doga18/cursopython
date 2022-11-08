# Esse seria o main.

from sys import path

#import aula99_package

import aula99_package.modulo
import aula99_package
from aula48_import_modulos_padrao import aula48_modularizacao_module

from aula99_package.modulo import soma_do_moulo, fala_oi
from aula99_package import modulo
from aula99_package.modulo import *



print(soma_do_moulo(1, 2))
print(aula99_package.modulo.soma_do_moulo(1, 2))
print(modulo.soma_do_moulo(3, 4))

print(variavel_modulo)

# print(*path, sep='\n')
# fala_oi()
# soma_do_moulo(1, 6)


print(aula99_package.dobra(2))
print(aula99_package.variavel_modulo, aula99_package.nova_variavel)

print(aula99_package.fala_oi())