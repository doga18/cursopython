print(
    'Você importou', __name__
)


def dobra(x):
    return x * 2


from .modulo import variavel_modulo, soma_do_moulo, nova_variavel


# Aqui neste caso, seria recomendavel utilizar o tudo/all * Exemplo:

from .modulo import *
from .modulo_b import *

