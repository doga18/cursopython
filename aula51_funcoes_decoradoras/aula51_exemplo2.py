def decorador1(funcao_simples1, *args, **kwargs):
    # print(f'decorador1 - função: {funcao_simples1}, args: {args}, kwargs: {kwargs}')

    def funcao_decorada1(*args, **kwargs):
        # print(f'função decorada1 - *args: {args}, **kwargs: {kwargs}')
        print('1#####')
        retorno_da_funcao1 = funcao_simples1(*args, **kwargs)
        print('1#####')
        return retorno_da_funcao1 + '"retorno1'

    return funcao_decorada1


def decorador2(funcao_simples2, *args, **kwargs):
    # print(f'decorador2 - função: {funcao_simples2}, args: {args}, kwargs: {kwargs}')

    def funcao_decorada2(*args, **kwargs):
        # print(f'função decorada2 - *args: {args}, **kwargs: {kwargs}')
        print('2-----')
        retorno_da_funcao2 = funcao_simples2(*args, **kwargs)
        print('2-----')
        return retorno_da_funcao2 + '"retorno2'

    return funcao_decorada2


@decorador2
@decorador1
def printar(a1, a2):
    print(f'função printar original - a1: {a1}, a2: {a2}')
    print(f'a1: {a2} - a2: {a1}')
    return 'return = funcionou'


print(printar('oi', 3))