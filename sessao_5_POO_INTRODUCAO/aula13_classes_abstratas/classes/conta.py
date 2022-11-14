from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if not isinstance(saldo, (int, float)):
            raise ValueError("saldo must be numeric")
        self._saldo = saldo

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("deposit value must be numeric")

        self._saldo += valor
        self.detalhes()

    def detalhes(self):
        print('\n')
        print(f'Agência: {self.agencia}', end=' ')
        print(f'Conta: {self.conta}', end=' ')
        print(f'Saldo: {self.saldo}', end=' ')
        print('\n')

    @abstractmethod
    def sacar(self, valor):
        pass