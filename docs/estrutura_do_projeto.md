# Estrutura do Projeto

Este documento descreve a organização de diretórios e arquivos do Flix API, explicando a responsabilidade de cada componente.

## Visão Geral

```
flix_api/
├── app/                    # Configuração central do projeto Django
│   ├── __init__.py         # Marca o diretório como pacote Python
│   ├── settings.py         # Configurações do Django e DRF
│   ├── urls.py             # Roteamento raiz — prefixa todas as APIs com /api/v1/
│   ├── permissions.py      # GlobalDefaultPermission — mapeamento HTTP → permissão Django
│   ├── wsgi.py             # Entry point WSGI para deploy
│   └── asgi.py             # Entry point ASGI para deploy assíncrono
├── actors/                  # App de atores
│   ├── models.py           # Modelo Actor (name, birthdate, nationality)
│   ├── serializers.py      # ActorSerializer (ModelSerializer simples)
│   ├── views.py            # ActorCreateListView, ActorRetrieveUpdateDestroyView
│   ├── urls.py             # Rotas /actors/ e /actors/<int:pk>/
│   ├── admin.py            # Registro do Actor no admin com list_display
│   ├── apps.py             # ActorsConfig
│   └── management/
│       └── commands/
│           └── import_actors.py  # Comando manage.py para importar atores de CSV
├── genres/                  # App de gêneros
│   ├── models.py           # Modelo Genre (name)
│   ├── serializers.py      # GenreSerializer
│   ├── views.py            # GenreCreateListView, GenreRetrieveUpdateDestroyView
│   ├── urls.py             # Rotas /genres/ e /genres/<int:pk>/
│   ├── permissions.py      # GenrePermissionClass (redundante — veja problemas conhecidos)
│   ├── tests.py            # Testes do módulo de gêneros (único app com testes)
│   └── admin.py, apps.py
├── movies/                  # App de filmes
│   ├── models.py           # Modelo Movie (title, genre FK, actors M2M, release_date, resume)
│   ├── serializers.py      # MovieSerializer, MovieModelSerializer, MovieListDetailSerializer, MovieStatsSerializer
│   ├── views.py            # MovieCreateListView, MovieRetrieveUpdateDestroyView, MovieStatsView
│   ├── urls.py             # Rotas /movies/, /movies/<int:pk>, /movies/stats/
│   └── admin.py, apps.py
├── reviews/                 # App de avaliações
│   ├── models.py           # Modelo Review (movie FK, stars com validação 0–5, comment)
│   ├── serializers.py      # ReviewSerializers (note: nome com "s" no plural)
│   ├── views.py            # ReviewCreateListView, ReviewRetrieveUpdateDestroyView
│   ├── urls.py             # Rotas /reviews/ e /reviews/<int:pk>/
│   └── admin.py, apps.py
├── authentication/          # App de autenticação JWT (sem modelo próprio)
│   ├── urls.py             # Rotas de token: obtain, refresh, verify
│   └── apps.py             # AuthenticationConfig
├── docs/                    # Documentação do projeto
├── manage.py                # Utilitário Django (DJANGO_SETTINGS_MODULE=app.settings)
├── pyproject.toml            # Dependências e metadados (uv)
├── requirements.txt         # Dependências exportadas para pip
├── requirementes_dev.txt    # Dependências de desenvolvimento (nome com typo)
├── uv.lock                  # Lock file do uv
├── actors.csv               # Dados de exemplo para import_actors
└── db.sqlite3               # Banco SQLite (versionado no git)
```

## Decisões Estruturais

### Apps na raiz do repositório

Todos os apps Django estão na raiz do repositório (e.g., `actors/`, `genres/`), não no padrão de subdiretório. Isso é configurado implicitamente pelo `manage.py` que aponta `DJANGO_SETTINGS_MODULE` para `app.settings`, e os apps são referenciados por seus nomes de pacote em `INSTALLED_APPS`.

### Módulo `app/` vs apps de domínio

O diretório `app/` contém apenas configuração e infraestrutura (settings, URLs raiz, permissions). Não possui modelos. Os quatro apps de domínio (`actors`, `genres`, `movies`, `reviews`) seguem um padrão uniforme de `models → serializers → views → urls`.

### Módulo `authentication/`

O app de autenticação não possui modelo nem views próprias. Ele serve apenas para registrar as rotas JWT do `rest_framework_simplejwt` sob o prefixo `/api/v1/authentication/`.

### Prefixo de rotas

Todas as rotas de API são montadas sob `/api/v1/` no `app/urls.py`:

```python
path('api/v1/', include('authentication.urls')),
path('api/v1/', include('genres.urls')),
path('api/v1/', include('actors.urls')),
path('api/v1/', include('movies.urls')),
path('api/v1/', include('reviews.urls')),
```

### Dependências entre apps

- `movies` depende de `genres` (FK) e `actors` (M2M) no modelo `Movie`.
- `reviews` depende de `movies` (FK) no modelo `Review`.
- `movies` depende de `reviews` no `MovieListDetailSerializer` e `MovieStatsView` (para calcular nota média).
- `actors` e `genres` são apps independentes, sem dependência entre si ou com outros apps.

## Relação com o Frontend

Esta API é o backend do **Flix App**, um dashboard disponível em [github.com/marcosilvaa/flix_app](https://github.com/marcosilvaa/flix_app). O dashboard consome todos os endpoints documentados em [Endpoints da API](endpoints_da_api.md) para gerenciar e visualizar filmes, atores, gêneros e avaliações.