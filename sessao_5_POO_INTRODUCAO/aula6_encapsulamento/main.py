"""

Encapsulamento, serve para proteger a aplicação escondendo.
Métodos e atributos public, protected, private
public = são atributos que podem ser acessados, dentro e fora da classe.
protected = são atributos que podem ser acessados, apenas dentro da classe ou das filhas daquela classe.
private = só está disponível dentro daquela classe.

_ protected (public_)
__ privado (_NOMEDACLASSE__nomeatributo) proibindo acesso fora da classe.

"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def listar_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(f'Cliente ID: {id}, com nome: {nome}')

    def apagar_cliente(self, id):
        del self.__dados['clientes'][id]


a1 = BaseDeDados()

a1.inserir_cliente(1, 'douglas')
a1.inserir_cliente(2, 'Silvia')
a1.inserir_cliente(3, 'gilson')


# print(a1.__dados)
print(a1.listar_clientes())
# a1.apagar_cliente(2)
print(a1.listar_clientes())

a1.__dados = 'outra coisa' # com proteção vc não acessa, para acessar confira abaixo.
print(a1.__dados)

# Acessando
print(a1._BaseDeDados__dados)
print(a1.dados)