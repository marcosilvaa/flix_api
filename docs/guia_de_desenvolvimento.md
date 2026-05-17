# Guia de Desenvolvimento

## Requisitos

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) (gerenciador de pacotes)

## Setup

```bash
# Instalar dependências
uv sync

# Criar ambiente virtual (alternativa sem uv)
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt

# Executar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Iniciar servidor
python manage.py runserver
```

> **Importante:** `DEBUG = False` por padrão. Para desenvolvimento local, altere para `True` em `app/settings.py`, caso contrário requisições serão rejeitadas a menos que o host esteja em `ALLOWED_HOSTS`. Atualmente `ALLOWED_HOSTS = ['*']`.

## Comandos Frequentes

```bash
# Servidor de desenvolvimento
python manage.py runserver

# Testes (apenas genres possui testes)
python manage.py test
python manage.py test genres

# Lint
python -m flake8 .

# Migrações
python manage.py makemigrations
python manage.py migrate

# Importar atores
python manage.py import_actors actors.csv

# Admin
python manage.py createsuperuser

# Produção
python manage.py collectstatic --noinput
```

## Configuração do flake8

O arquivo `.flake8` na raiz configura:

```ini
[flake8]
exclude = .venv
ignore = E501
```

Ignora linhas longas (`E501`) e exclui o diretório `.venv`.

## Banco de Dados

O projeto usa SQLite por padrão (`db.sqlite3` na raiz). O arquivo está versionado no git (`.gitignore` tem a linha `#db.sqlite3` comentada).

Para produção, recomenda-se trocar para PostgreSQL ou MySQL em `app/settings.py`.

## Adicionar um Novo App

1. Criar o diretório na raiz do projeto com `models.py`, `serializers.py`, `views.py`, `urls.py`, `admin.py`, `apps.py`.
2. Registrar em `INSTALLED_APPS` em `app/settings.py`.
3. Incluir as URLs em `app/urls.py` com `path('api/v1/', include('novo_app.urls'))`.
4. Aplicar permissões nas views: `permission_classes = (IsAuthenticated, GlobalDefaultPermission,)`.
5. Criar e aplicar migrações: `python manage.py makemigrations && python manage.py migrate`.

## Fluxo de Trabalho Recomendado

1. Criar branch com nome descritivo: `feat/recurso` ou `fix/problema`
2. Commits pequenos com mensagens no formato: `tipo(escopo): descrição curta`
3. Testar com `python manage.py test` e `python -m flake8 .`
4. Pull request para revisão