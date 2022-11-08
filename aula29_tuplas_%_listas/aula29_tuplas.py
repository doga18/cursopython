t1 = (1,2,3,'douglas','luiz')
t2 = 6,9,58,4

#concatenando
t3 = t1+t2

print(type(t1))
print(t1)
print(t1[3])
print(t1[2:]) #Fatiando!

for v in t1:
    print(v)

print(t3)
valor1, valor2, valor3, *_ = t3
print(valor1)
print(*_)

#multiplicar tuplas

tupla1 = (1,5,9,6,'israel','luana') *20
print(tupla1)

#convertendo tulpa pra lista.

n1 = (1,2,3,4,5)
n1 = list(n1) #Transformando a tupla em lista, para poder modificar os valores!
print(n1)
n1[2] = 3000
print(n1)
n1 = tuple(n1) #Transformando em Tupla novamente.