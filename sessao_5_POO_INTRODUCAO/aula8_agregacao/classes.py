# Relação de Agregação

class CarrinhoDeCompras:
    def __init__(self):
        self.produto = []

    def inserir_produto(self, produto):
        self.produto.append(produto)

    def lista_produto(self):
        for p in self.produto:
            print(p.nome, p.valor)

    def soma_total(self):
        total = 0
        for p in self.produto:
            total += p.valor
        return total


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor