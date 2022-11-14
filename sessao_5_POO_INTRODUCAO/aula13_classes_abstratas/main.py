"""
Polimorfismo é o princípio que permite que classes derivadas de uma mesma superclasse tenha métodos
iguais (de mesma assinatura) mas comportamentos diferentes.

Mesma assinatura = Mesma quantidade e tipo de parâmetro.
"""

from classes.cp import *
from sessao_5_POO_INTRODUCAO.aula13_classes_abstratas.classes.cc import ContaCorrente

cp = ContaPoupanca(123, 112, 20021.65)

cp.sacar(20021.67)
# cp.detalhes()

c1 = ContaCorrente(22331, 22123, 2000)

c1.sacar(1100)
c1.sacar(345)
c1.sacar(555)
c1.sacar(300)
c1.sacar(700)
c1.sacar(1)