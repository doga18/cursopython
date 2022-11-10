class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        # Para verificar qual classe chama.
        self.nomeclasse = self.__class__.__name__


    def falar(self):
        print(f'{self.nomeclasse} {self.nome} está falando...')


# Quando você colocar o (Classe) você quer dizer que tal classe, herda da classe dos parenteses.
class Client(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando...')


class Aluno(Pessoa):
    def estudando(self):
        print(f'{self.nomeclasse} estudando...')
