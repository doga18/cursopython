nome = 'Douglas'
idade = 42
altura = 1.69
peso = 78
ano_atual = 2022
ano_nasc = ano_atual - idade
imc = peso / altura ** 2

print(f'O Paciente {nome}, tem {idade} anos de idade, com nascimento em {ano_nasc} e tendo seu IMC de {imc:.2f}')