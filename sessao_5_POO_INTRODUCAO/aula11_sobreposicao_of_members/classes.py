class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        # Para verificar qual classe chama.
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} {self.nome} está falando... Padrão Pessoa.')


# Quando você colocar o (Classe) você quer dizer que tal classe, herda da classe dos parenteses.
class Client(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} {self.nome} comprando...')

    def falar(self):
        print(f'Classe Client Padrão {self.nome} está falando...')


class ClientVIP(Client):
    # Isso sobrepoe métodos de classes herdadas.
    # Sobrepoe, a function falar de pessoa, para a ClientVIP.
    def falar(self):
        # Quando se coloca o Super, o método herdado, terá prioridade.
        # Após isso, irá executar os demais passos desse método sobreposto.
        # Super procurará o primeiro método com o mesmo nome.
        super().falar()
        # Caso Queria especificar, precisa utlizar da seguinte forma.
        Client.falar(self)
        Pessoa.falar(self)
        print('E além disso esse cliente é VIP')

    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        Client.falar(self)
        print(f'{self.nome} com sobrenome {self.sobrenome}!')