from classes import *

p1 = Escritor('Douglas')
p2 = Caneta('Bic')
p3 = MaquinaDeEscrever()

print(p1.nome)
print(p2.marca)
print(p3)

p1.ferramenta = p3

p1.ferramenta.escrever()

