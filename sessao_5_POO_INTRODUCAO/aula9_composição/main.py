from classes import *

c1 = Cliente('Douglas', 21)
c1.insere_enderecos('Florianopolis', 'SC')
print(c1.nome)
c1.lista_enderecos()
del c1
print()

c2 = Cliente('Luiz', 31)
c2.insere_enderecos('São josé', 'SC')
print(c2.nome)
c2.lista_enderecos()
del c2
print()

c3 = Cliente('Sil', 45)
c3.insere_enderecos('Bernardo', 'SP')
print(c3.nome)
c3.lista_enderecos()
del c3
print()





# print(f'O cliente {c1.nome} tem {c1.idade} anos de vida e mora em {c1.lista_enderecos()}')