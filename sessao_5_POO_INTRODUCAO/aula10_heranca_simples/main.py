from classes import *

"""
Associação - USA | Agregação - Tem | Composição - É Dono | Herança - É
"""

# Exemplo de Cliente que está herando de Pessoa.
c1 = Client('Douglas', 21)
print(c1.nome)


""" Exemplo de um Aluno que é uma pessoa, então herda da classe Pessoa """
aluno1 = Aluno('Gilson', 45)
print(aluno1.nome)

aluno1.falar()

c1.comprar()
aluno1.estudando()