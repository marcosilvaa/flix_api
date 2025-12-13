# Estrutura do Projeto

Este documento descreve a estrutura de diretórios e arquivos do projeto Flix API, explicando a organização geral e o propósito de cada componente.

## Visão Geral da Estrutura

```
flix-api/
├── .gitignore          # Arquivos e diretórios ignorados pelo Git
├── .python-version     # Versão específica do Python usada no projeto
├── main.py             # Arquivo inicial do projeto (não usado diretamente no Django)
├── manage.py           # Script de utilitário Django para tarefas administrativas
├── pyproject.toml      # Configuração do projeto Python (gerenciamento de dependências)
├── README.md           # Informações básicas sobre o projeto
├── requirements.txt    # Dependências do projeto
├── uv.lock             # Lock file do gerenciador de pacotes uv
├── actors/             # Módulo de atores/famosos
├── app/                # Configurações centrais do Django
├── authentication/     # Sistema de autenticação JWT
├── docs/               # Documentação do projeto
├── genres/             # Módulo de gêneros de filmes
├── movies/             # Módulo de filmes
└── reviews/            # Módulo de avaliações
```

## Descrição das Pastas

### app/
Contém os arquivos de configuração principais do Django:
- `settings.py` - Configurações do projeto Django e REST Framework
- `urls.py` - Roteamento principal da aplicação
- `wsgi.py` e `asgi.py` - Configurações para execução do servidor
- `permissions.py` - Lógica central de permissões da aplicação

### actors/, genres/, movies/, reviews/
Cada módulo representa uma parte do domínio do sistema e segue a mesma estrutura:
- `models.py` - Definição das entidades do banco de dados
- `serializers.py` - Serialização dos dados para JSON
- `views.py` - Lógica de negócio das requisições HTTP
- `urls.py` - Rotas específicas do módulo
- `admin.py` - Configurações da interface administrativa Django
- `apps.py` - Configurações do aplicativo Django
- `tests.py` - Testes unitários

### authentication/
Sistema de autenticação baseado em JWT:
- Utiliza `rest_framework_simplejwt`
- Define rotas para obtenção, atualização e verificação de tokens

## Tecnologias Utilizadas

- Python 3.13+
- Django 5.2.7
- Django REST Framework 3.16.1
- SQLite (banco de dados default)
- JWT para autenticação
- uv como gerenciador de pacotes

## Gerenciamento de Dependências

O projeto utiliza `pyproject.toml` para definição de dependências e `uv.lock` para garantir versões consistentes entre ambientes.