class Pessoa:
    # Variavel de Classe
    vc = 123

    def __init__(self):
        # Variavel de instância.
        self.vc = 321666


a1 = Pessoa()
a2 = Pessoa()
a3 = Pessoa()

Pessoa.vc = 321

a1.vc = 345

print(a1.vc)
print(Pessoa.vc)

print(a1.__dict__)
print(a2.__dict__)
print(Pessoa.__dict__)
print(a3.vc)