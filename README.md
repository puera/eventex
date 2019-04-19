# Eventex

Sistema de Eventos encomendando pela Morena.

[![Build Status](https://travis-ci.org/puera/eventex.svg?branch=master)](https://travis-ci.org/puera/eventex)
[![Maintainability](https://api.codeclimate.com/v1/badges/82593eacca7658fcbf1f/maintainability)](https://codeclimate.com/github/puera/eventex/maintainability)
## Como desenvolver?

1- Instale git e python3
```console
sudo apt-get install git python3-pip python3-dev python3-setuptools \
python3-venv
```
2- Instale o virtualenvwrapper.
```console
sudo pip3 install virtualenvwrapper
```
3- Crie o diretório de projeto e ajuste a permissão.
```console
sudo mkdir -p /var/projetos/.virtualenvs
sudo chown -R $USER:$USER /var/projetos/
```
4- Edite o arquivo .bashrc e adicione ao seu final as configurações abaixo para o virtualenvwrapper.
```console
nano /home/$USER/.bashrc

export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=/var/projetos/.virtualenvs
export PROJECT_HOME=/var/projetos
source /usr/local/bin/virtualenvwrapper.sh
```
5- Carregue as config do virtualenvwrapper.
```console
source /home/$USER/.bashrc
```
6- Clone o repositório do git.
```console
cd /var/projeto
git clone git@github.com:puera/eventex.git
```
7- Crie o ambiente virtual para o eventex.
```console
mkvirtualenv -a /var/projetos/eventex eventex
```
8- Ative o ambiente virtual eventex.
```console
workon eventex
```
9- Instale as dependências do eventex.
```console
pip install -r /var/projetos/eventex/requirements.txt
```
10- Ajuste as permissões.
```console
eval $(echo "sudo chown -R $USER:$USER /var/projetos/")
```
11- Configure o arquivo .env.
```console
nano /var/projetos/eventex/.env

SECRET_KEY==SUA KEY
DEBUG=[True/False]
ALLOWED_HOSTS=Host permitidos
EMAIL_BACKEND=Backend do email
EMAIL_HOST=[servidor smtp]
EMAIL_PORT=[porta]
EMAIL_USE_TLS=[True/False]
EMAIL_HOST_USER=[user]
EMAIL_HOST_PASSWORD=[pass]
```


