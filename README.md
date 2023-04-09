Lista Criativa

Descrição
Este projeto é uma lista de tarefas criativas desenvolvida com Python, Django e MySQL. Ele permite que você adicione, visualize e marque tarefas como concluídas em um ambiente de desenvolvimento local.

Pré-requisitos
Antes de começar a usar este projeto, você precisará ter as seguintes ferramentas instaladas em sua máquina:

Python 3.6 ou superior
pip
MySQL

Instalação
Clone o repositório para o seu computador:
git clone https://github.com/seu-usuario/lista-criativa.git

Crie um ambiente virtual para o projeto:
python -m venv venv

Ative o ambiente virtual:
source venv/bin/activate

Instale as dependências do projeto:
pip install -r requirements.txt

Crie um banco de dados no MySQL e configure as informações de conexão no arquivo myproject/settings.py do projeto:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_banco_de_dados',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

Crie as tabelas do banco de dados executando as migrações do Django:
python manage.py migrate

Execute o servidor de desenvolvimento do Django:
python manage.py runserver
Abra um navegador da web e navegue até http://localhost:8000/todo/ para visualizar a lista de tarefas criativas.

Contribuição
Se você quiser contribuir para este projeto, siga os seguintes passos:

Faça um fork do repositório.
Crie um branch para sua nova feature (git checkout -b feature/nome-da-sua-feature).
Implemente sua feature e faça os commits (git commit -am 'Adiciona nova feature').
Envie as alterações para o seu repositório (git push origin feature/nome-da-sua-feature).
Crie um Pull Request para o repositório principal.

testando