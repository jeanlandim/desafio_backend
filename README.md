# Desafio backend

# Descrição

Implementada a API RESTful utilizando django e django rest framework tendo as seguintes funcionalidades:

* É capaz de receber um texto e um título
* Guarde o texto e o título na BD SQLite3
* É capaz de pesquisar por título E/OU pelo texto (tanto via curl e pela página inicial do app)
* Retorne o texto e título dos resultados encontrados (veja a página inicial do app)

# Especificações

**** O projeto foi criado e entregue por meio de algum gerenciador de repositórios Git (github, gitlab, bitbucket ou outros).
* A API foi implementada utilizando Django + Django rest framework
* Utilizado o Git Flow para controlar a implementação das features
* Utilizado algum sistema de ambientes virtuais (virtualenv)
* Utilizado sqlite como BD
* Utilizado o ORM do django
* Utilizado o django-admin startproject para iniciar seu projeto

# Como testar este repositório

```
$ git clone https://github.com/jeanlandim/desafio_backend
$ cd desafio_backend
$ mkvirtualenv desafio_backend
$ pip install -r requirements.txt
$ python manage.py makemigrations && python manage.py migrate && python manage.py runserver
```
Abra o navegador em http://localhost:8000 para busca de texto ou titulo, e utilize o endereço http://localhost:8000/api-textos/ para inserção, atualização e remoção dos itens da API

Para testes na API:

```
$ python3 manage.py test
```

Aguardo retorno, abraço!
