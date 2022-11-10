from classes import *

car = CarrinhoDeCompras()

print(car)

p1 = Produto('Camiseta', 50)
p2 = Produto('Camiseta Br', 500)
p3 = Produto('Camiseta RE', 201)

car.inserir_produto(p1)
car.inserir_produto(p2)
car.inserir_produto(p3)

car.lista_produto()
print(car.soma_total())