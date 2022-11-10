from classes import *
from sessao_5_POO_INTRODUCAO.aula9_composição.classes import Cliente

"""
Associação - USA | Agregação - Tem | Composição - É Dono | Herança - É
"""

# Exemplo de Cliente que está herando de Pessoa.
c1 = Client('Douglas', 21)
c1.comprar()
print(c1.nome)

c2 = ClientVIP('Silvia', 24, 'Serafim')
c2.falar()