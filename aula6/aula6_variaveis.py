nome = 'douglas'
idade = 32
altura = 1.70
e_maior = idade > 18
data_1 = True
data_atual = 2019
peso = 80
imc = peso / altura ** 2

print('Nome: ', nome)
print('Idade: ', idade)
print('Altura: ', altura)
print('É maior: ', e_maior)

print("O nome do Paciente é "+str(nome)+", ele tem "+str(idade)+" anos de vida, com peso de "+str(peso)+" Kg, e sua altura é de "+str(altura)+" cm, sendo assim seu imc é de "+str(imc))

# facilitando as várias no código.

print(f'O nome do paciente é {nome}, esse paciente tem {idade} anos de vida, com peso de {peso} kg, sua altura é de {altura} cm e tem seu IMC de {imc:.2f}')
# outro método, LEMBRANDO QUE A FORMAÇÃO VOCÊ COLOCA NO CAMPO, E NÃO ONDE CHAMA A VARIÁVEL!
print('O nome do paciente é {}, esse paciente tem {} anos de vida, com peso de {} kg, sua altura é de {} cm e tem seu IMC de {:.2f}'.format(nome, idade, peso, altura, imc))

print('O nome do paciente é {0} {0} {1} {3}{4}'.format(nome, idade, peso, altura, imc))
print('{n} {m} {o} {q} {b}'.format(n=nome, m=idade, o=peso, q=altura, b=imc))
