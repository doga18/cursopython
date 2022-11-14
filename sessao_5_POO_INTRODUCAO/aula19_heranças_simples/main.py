"""

Estrutura de Herança sempre de cima pra baixo.

Animal Base Método respisrar -> Respirar
    Lobo (animal) Herda Respirar, Especifico Uivar
        Cachorro (Lobo) Herda Respirar, Herda Uivar, Espefico Latir.
            (Charro é um cachorro também é um lobo que também é um animal.


Fazendo o exemplo, embora complexo, inverso.

    Biblioteca
        Interface(Biblioteca) -> metodo_da_interface


"""

from classes.interface import Interface

# a1 = Interface()
# a1.metodo_da_interface()

a2 = Interface()
a2.chama_metodo_da_interface()
