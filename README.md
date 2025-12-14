# Flix API

API para gerenciamento de filmes, atores, gêneros e avaliações cinematográficas.

## Sobre o Projeto

Flix API é uma aplicação Django REST Framework que fornece endpoints para gerenciar informações sobre filmes, atores, gêneros e avaliações. O projeto foi desenvolvido com foco em boas práticas de desenvolvimento e arquitetura limpa.

## Tecnologias Utilizadas

- Python 3.13+
- Django 5.2.7
- Django REST Framework 3.16.1
- SQLite (banco de dados default)
- JWT para autenticação

## Configuração do Ambiente

### Requisitos
- Python 3.13 ou superior
- uv (gerenciador de pacotes)

### Instalação Inicial
```bash
# Clonar o repositório
git clone <url-do-repositorio>
cd flix_api

# Criar ambiente virtual
python -m venv .venv
source .venv/bin/activate  # No Linux/Mac
# ou
.venv\Scripts\activate     # No Windows

# Instalar dependências
uv sync
# ou
pip install -r requirements.txt
```

### Iniciar o Projeto
```bash
# Executar migrações
python manage.py migrate

# Criar superusuário (opcional)
python manage.py createsuperuser

# Iniciar o servidor
python manage.py runserver
```

## Documentação

Para mais detalhes sobre o projeto, consulte a documentação completa na pasta [docs](./docs/README.md).