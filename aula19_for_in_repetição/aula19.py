'''
For in Python
Iterando strings com formato
Função range (start=0, stop, step=1
'''
texto = 'Python'

for n, letra in enumerate(texto):
    print(n, letra)

# de forma positiva

for conte in range(15, 100, 4):
    print(conte)
print("separador!")

# de forma negativa

for conte_negativo in range(115, 100, -4):
    print(conte_negativo)
print("separador!")

for conte_1 in range(100):
    if conte_1 % 8 == 0:
        print(conte_1)

texto = 'Python'
nova_string = ''

# continue - pula para o proximo laço
# break, para o laço.

for letra in texto:
    if letra == 't':
        continue
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string +=letra

print(nova_string)
