# Para não termos problemas ao colocar caminhos do Windows, sempre colocar r antes do caminho, exemplo.

addres_file_windows = r'C:\Documents\something'

import shutil
import os

caminho_original = r'E:\FFOutput\saida'
caminho_novo = r'E:\FFOutput\saida2'

try:
    os.mkdir(caminho_novo)
    print(f'Pasta Sendo Criada.')
    arquivo1 = r'\teste1.txt'
    arquivo2 = r'\teste2.txt'
    arquivo3 = r'\teste3.txt'

    with open(caminho_novo + arquivo1, '+a', encoding='utf8') as arquivo:
        msg1 = f'Estou aqui escrevendo no arquivo: %s' % arquivo1
        arquivo.write(msg1)

    with open(caminho_novo + arquivo2, '+a', encoding='utf8') as arquivo:
        msg1 = f'Estou aqui escrevendo no arquivo: %s' % arquivo3
        arquivo.write(msg1)

    with open(caminho_novo + arquivo3, '+a', encoding='utf8') as arquivo:
        msg1 = f'Estou aqui escrevendo no arquivo: %s' % arquivo3
        arquivo.write(msg1)


except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')

for root, dirs, files in os.walk(caminho_original):
    for f in files:
        old_file_path = os.path.join(root, f)
        new_file_path = os.path.join(caminho_novo, f)
        # print(old_file_path)

        # Colocando uma validação para copiar somente extensções, pode ser utilizado inclusive espressões regulares.
        if '.srt' in f:
            shutil.copy(old_file_path, new_file_path)
            print(f'Arquivo "{f}" copiado do diretório "{root}", para o diretório "{caminho_novo}".')

        # Aqui de fato é onde é movido os arquivos, move também sobreescreve o arquivo.
        # shutil.move(old_file_path, new_file_path)
        # print(f'Arquivo {f} movido com sucesso.')

print('')
print('')

contador_delete = 0
# Criando um for para deletar arquivos específicos com extensão.
for root, dirs, files in os.walk(caminho_novo):
    for f in files:
        contador_delete += 1
        old_file_path = os.path.join(root, f)
        new_file_path = os.path.join(caminho_novo, f)
        # delete_addres = (caminho_novo, f)
        nome_arquivo, ext_arquivo = os.path.splitext(f)
        # print(nome_arquivo, ext_arquivo)
        # print(f'{ext_arquivo}')
        if '.srt' in f:
            os.remove(caminho_novo)
            print(f'Deletando aquivos que tenham extensão {ext_arquivo}.\n{nome_arquivo} Deletado.')


print('')
if contador_delete <= 1:
    print(f'{contador_delete} arquivo deletado com sucesso.')
else:
    print(f'{contador_delete} arquivos deletados com sucesso.')