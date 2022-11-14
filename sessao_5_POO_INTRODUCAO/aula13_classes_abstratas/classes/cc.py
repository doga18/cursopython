from classes.conta import Conta


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=1000):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if self._saldo < valor:
            if (self._saldo + self._limite) < valor:
                print(f'Saldo Insuficiente, Saldo atual: {self._saldo}')
                super().detalhes()
                return
            print(f'Atenção, seu saldo está negativo, efetuando saque: {valor}.')

        print(f'Saldo {self._saldo}, valor a ser sacado: {valor} ')
        self._saldo -= valor
        print(f'Saldo restante: {self._saldo}.')
        super().detalhes()