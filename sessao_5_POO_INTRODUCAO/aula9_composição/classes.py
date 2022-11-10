class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_enderecos(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado)) # aqui estou passando os dados para a class endereco pra ela tratar. ### COMPOSIÇÃO

    def lista_enderecos(self):
        for p in self.enderecos:
            print(f'Cidade: {p.cidade} e Estado: {p.estado}.')

    def __del__(self):
        print(f'{self.nome} FOI APAGADO')


class Endereco:
    def __init__(self, cidade, estado): # Como o init tá aqui, vai receber esses dados e construir.
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade}/{self.estado} FOI APAGADO')