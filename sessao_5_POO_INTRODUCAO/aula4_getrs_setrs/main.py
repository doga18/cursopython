class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco % (percentual / 100))

    # Getter Método Decorador
    @property
    def preco(self):
        return self._preco

    # Setter Método Decorador
    @preco.setter
    def preco(self, valor):
        # Quando o isinstance está sem o not, significa, que Se For oque estou vendo faça tal coisa.
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, name_value):
        if isinstance(name_value, str):
            name_value = name_value.replace('12', '')
            self._nome = name_value
        elif isinstance(name_value, (float, int)):
            name_value = str(name_value)
            self._nome = name_value



p1 = Produto('Carmisa', 30)
p1.desconto(10)
print(p1.preco)

p2 = Produto(54, 'R$15')
p2.desconto(10)
print(p2.preco)
print(f'Nome: {p2.nome}')