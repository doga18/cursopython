"""
while / else
contadores
acumuladores
"""
contador = 0
acumulador = 2

while contador <= 100:
    print(contador, acumulador)
    acumulador = acumulador + contador
    contador += 1
else:
    print(f'Terminei o While a condição ficou {contador} ou seja maior que a condição, tornando-se False e cheguei no else.')