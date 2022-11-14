import os

# Função para contar os bytes.
def bytes_description(filesize):
    base_bytes = 1024
    # KiloBytes
    kilo_bytes = base_bytes
    # Megabytes
    megabytes = base_bytes ** 2
    # Gigabytes
    gigabytes = megabytes ** 3
    # TeraBytes
    terabytes = gigabytes ** 4
    # PentaBytes
    pentabytes = terabytes ** 5

    if filesize < kilo_bytes:
        filesize = base_bytes
        text = 'Bytes'
    elif filesize < megabytes:
        filesize /= kilo_bytes
        text = 'KiloBytes'
    elif filesize < gigabytes:
        filesize /= megabytes
        text = 'Megabytes'
    elif filesize < terabytes:
        filesize /= gigabytes
        text = 'Gigabytes'
    elif filesize < pentabytes:
        filesize /= terabytes
        text = 'TeraBytes'
    else:
        filesize /= pentabytes
        text = 'PentaBytes'

    filesize = round(filesize, 2)
    # return f'Tamanho {filesize} {text}'
    # Deixando mais bonito podemos substituir o ponto para vírgula.
    return f'Tamanho {filesize} {text}'.replace('.', ',')

# tamanho_teste = 10485761
# print(bytes_description(tamanho_teste))

# Variaveis definidas
# caminho_procura = 'E:\\cursopython\\sessao_6_modules_python\\aula3_percorrer_files_and_dir\\'
# termo_procura = '09'

# Definindo o arquivo a procurar:
termo_procura = input('Digite o termo que deseja procurar: ')
caminho_procura = input('Digite o local que deseja procurar: ')



# Método os.walk onde ele caminha nos diretórios, nele e nas subpastas.
contador = 0
for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                contador += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)
                # print(tamanho, nome_arquivo, ext_arquivo)
                print()
                print(f'Encontrei o arquivo procurado: {arquivo}')
                print(f'Caminho do arquivo: {caminho_completo}')
                print(f'Nome do arquivo: {nome_arquivo}')
                print(f'Extesão do Arquivo: {ext_arquivo}')
                print(f'Tamanho do Arquivo: {bytes_description(tamanho)}')
            except PermissionError as e:
                print(f'Sem permissão de acesso, para procurar o arquivo {termo_procura}, no diretório {caminho_procura}, temos permissão de acesso? Error Num: {e}')
            except FileNotFoundError as e:
                print(f'Arquivo não encontrado no {caminho_procura} informado. Error Num: {e}')
            except Exception as e:
                print(f'Erro desconhecido: {e}')

print()
if contador == 1:
    print(f'{contador} arquivo encontrado.')
elif contador > 1:
    print(f'{contador} arquivos encontrados.')



