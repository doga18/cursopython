from classes.conta import Conta


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self._saldo < valor:
            print(f'Saldo Insuficiente, Saldo atual: {self._saldo}')
            super().detalhes()
            return

        print(f'Saldo {self._saldo}, valor a ser sacado: {valor} ')
        self._saldo -= valor
        print(f'Saldo restante: {self._saldo}.')
        super().detalhes()



