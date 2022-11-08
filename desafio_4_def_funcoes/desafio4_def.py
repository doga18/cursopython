def mostrar_nome(nome, saudacao):
    msg = f'Olá, {saudacao}, Seja bem vindo ao sistema {nome}'
    return msg

print(mostrar_nome('Douglas','Boa noite'))

# def soma_de_numeros():
#     n1 = input('Insira o primeiro número: ')
#     n2 = input('Insira um segundo número: ')
#     n3 = input('Insira um terceiro número: ')
#
#     result = int(n1) + int(n2) + int(n3)
#
#     exibir = print(result)
#
#     return exibir
#
# soma_de_numeros()

def valor_percentual(valor, percentual):
    retorno = print(valor + (valor * percentual / 100))
    return retorno

valor_percentual(50, 10)

def fizzbuzz(num):
    if num % 3 == 0 & num % 5 == 0:
        return 'FizzBuzz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    else:
        return num

def fizzbuzz_mais_limpa(n):
    if n % 3 == 0 & n % 5 == 0:
        return f'FizzBuzz, {n} é divisível por 3 e 5.'
    if n % 5 == 0:
        return f'Buzz, {n} é divisível por 5.'
    if n % 3 == 0:
        return f'Fizz, {n} é divisível por 3'
    return f'{n} Não foi divisível por nenhuma das condições anteriores.'

print(fizzbuzz(15))
print(fizzbuzz_mais_limpa(15))

from random import randint

for i in range(100):
    aleatorio = randint(0, 100)
    print(fizzbuzz_mais_limpa(aleatorio))



