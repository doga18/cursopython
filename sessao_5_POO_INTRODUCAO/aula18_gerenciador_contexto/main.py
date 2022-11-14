"""
class Arquivo:
    def __init__(self, arquivo, modo):
        print('Init')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('Entrou na classe')
        return self.arquivo

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('Saiu na classe')
        self.arquivo.close()


with Arquivo('asd.txt', 'w') as arquivo:
    arquivo.write('alguma coisa')
"""

from contextlib import contextmanager

@contextmanager
def abrir(arquivo, modo):
    try:
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        arquivo.close()


with abrir('teste1.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
