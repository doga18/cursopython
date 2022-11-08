# Funções decoradoras e decoradores.
# Decorar = Adicionar, Remover, Restringir, Alterar,
# Funções decoradores são funções que decoram outras funções.
# Decoradores são usados para fazer o Python usar as funções decoradoas em outras funções.

def criar_function(func):
    def interna(*args, **kwargs):
        #
        print('Vou te decorar')
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora foi decorada.')
        #
        return resultado
    return interna


@criar_function
def inverte_string(string):
    return string[::-1]


def is_string(valor):
    if not isinstance(valor, str):
        raise TypeError('O valor informado não é uma String.')


var = 'serafim'


inverte_string_checando_parametro = criar_function(inverte_string)


invertida = inverte_string_checando_parametro('123DouglAs')

# invertida2 = inverte_string_checando_parametro(123)

print(invertida)
# print(invertida2)
print('#')
print(inverte_string(var))
print('#')
