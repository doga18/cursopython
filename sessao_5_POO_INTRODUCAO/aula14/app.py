"""
Polimorfismo é o princípio que permite que classes derivadas de uma mesma superclasse tenha métodos
iguais (de mesma assinatura) mas comportamentos diferentes.

Mesma assinatura = Mesma quantidade e tipo de parâmetro.
"""

from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def falar(self, msg): pass


class B(A):
    def falar(self, msg):
        print(f'B está falando {msg}')


class C(A):
    def falar(self, msg):
        print(f'C está falando {msg}')


a1 = B()
a2 = C()

a1.falar('um assunto')
a2.falar('outro assunto')