# Ambientes virtuais em Python (venv)
# Um ambiente virtual carrega toda a sua instalação
# do Python para uma pasta no caminho escolhido.
# Ao ativar um ambiente virtual, a instalação do
# ambiente virtual será usada.
# venv é o módulo que vamos usar para
# criar ambientes virtuais.
# Você pode dar o nome que preferir para um
# ambiente virtual, mas os mais comuns são:
# venv env .venv .env

"""Criando o ambiente virtual.

Linux

. ambiente/bin/activate  == Ativar
. ambiente/bin/deactivate == Desativar

Windows

.\Scripts\activate Ativando
.\Scripts\deactivate Desativando
No windows:

python.exe -m pip install pacote

Linux UNIX

python.exe -m pip install pacote / ex pymysql/django
desinstalar, uninstall pacote / uninstall pymysql

Buscando versões de pacote no pip.

pip index versions pymysql

Para instalar, voce usa, pip install pymysql==0.3

Para a versão 0.3

pip freeze server para pegar o atual ambiente que você tem e congelar esse ambiente nas versões dos módulos utilizados
e com ele que se gera o requirements

para montar um ambiente apartir do requirements você usa o comando.

pip install -r requirements.txt

"""