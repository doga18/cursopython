"""
While em pythons
realiza enquanto ação for true
"""
# cond = True
# while cond:
#     nome = input("Qual seu nome? ")
#     qtd_letras = len(nome)
#     if qtd_letras < 4:
#         print(f'O nome digitado é inválido, esse nome possui {qtd_letras} letras.')
#     else:
#         print(f'Olá {nome}!')
#         cond = False
# print("Sai do loop.")

x = 0

while x <= 10:
    if x == 3:
        x += 1
        """Aqui podemos colocar o continue ou o break, break, para todo o loop e sai dele ao encontrar a condição, continue, faz pular caso localiza a condição."""
        break
        #continue
    print(x)
    x+=1

print('Terminou\n\n\n')

u = 0 # coluna
y = 0 # linha

while u < 10:
    y = 0
    while y < 5:
        print(f'U Vale {u} e Y vale {y}')
        y += 1
    u += 1

print('Acabou')