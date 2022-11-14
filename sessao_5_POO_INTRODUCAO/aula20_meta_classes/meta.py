"""
Em python tudo é um objeto: incluindo classes.
Metaclasses são as "classes" que criam classes.
type é uma metaclasse (!!!???)

"""


# Meta Classe

class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if 'b_fala' not in namespace:
            print(f'Oi, você precisa criar o método b_fala em {name}')
        else:
            if not callable(namespace['b_fala']):
                print(f'b_fala precisa ser um métdo, não atributo em {name}')

        print(namespace)
        return type.__new__(mcs, name, bases, namespace)


# Exemplo de herança inversa.

class A(metaclass=Meta):
    def fala(self):
        self.b_fala()


class B(A):
    teste = 'Valor1'
    b_fala = 'Wow'
    # def b_fala(self):
    #     print(f'Oi eu sou o B, classe: {__class__.__name__}')
    def seila(self):
        pass


a1 = B()




