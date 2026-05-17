# Problemas Conhecidos

Este documento registra bugs, inconsistências e pontos de atenção identificados no código.

## Inconsistências

### Mensagens de validação com valores errados

Em `movies/serializers.py`, `MovieModelSerializer`:

- `validate_release_date`: rejeita anos < 1900, mas a mensagem de erro diz "não pode ser anterior à **1990**" (deveria dizer 1900).
- `validate_resume`: rejeita textos > 500 caracteres, mas a mensagem de erro diz "não pode ser maior do que **200** caracteres" (deveria dizer 500).

### Nome do serializer de Review

Em `reviews/serializers.py`, a classe se chama `ReviewSerializers` (plural) em vez de `ReviewSerializer`. O nome no singular é a convenção do DRF e é usado em todos os outros apps do projeto.

### Trailing slash inconsistente

As URLs de detalhe são inconsistentes:

- `/api/v1/genres/<int:pk>/` — com barra final
- `/api/v1/actors/<int:pk>/` — com barra final
- `/api/v1/movies/<int:pk>` — sem barra final
- `/api/v1/reviews/<int:pk>` — sem barra final

## Código Morto

### GenrePermissionClass

O arquivo `genres/permissions.py` contém `GenrePermissionClass`, que implementa o mapeamento HTTP → permissão manualmente com `if/elif`. No entanto, as views em `genres/views.py` usam `GlobalDefaultPermission` de `app/permissions.py`, que faz o mesmo mapeamento dinamicamente. Essa classe nunca é importada ou usada.

### MovieSerializer (não-ModelSerializer)

Em `movies/serializers.py`, a classe `MovieSerializer` é um `serializers.Serializer` manual com campos explícitos. Ela **não é usada** em nenhuma view — as views usam `MovieModelSerializer` (para escrita) e `MovieListDetailSerializer` (para leitura). É possivelmente um artefato de desenvolvimento.

### Arquivos README.md por app

Cada app contém um `README.md` com documentação em inglês dos arquivos do módulo. Esses arquivos estão desatualizados em relação ao código atual (e.g., o `movies/README.md` descreve serializers que foram alterados).

## Dependências

### flake8 como dependência de produção

`flake8` está em `pyproject.toml` como dependência de produção, quando deveria ser apenas de desenvolvimento. O arquivo `requirementes_dev.txt` (com typo no nome) também lista `flake8==7.3.0`.

### Arquivo de dev requirements com typo

O arquivo `requirementes_dev.txt` (na raiz) tem um typo: deveria ser `requirements_dev.txt`.

## Configuração

### DEBUG = False em desenvolvimento

O `app/settings.py` tem `DEBUG = False` por padrão, o que pode causar problemas em desenvolvimento local (erro 400 para ALLOWED_HOSTS não listados). Isso é mitigado por `ALLOWED_HOSTS = ['*']`, mas em conjunto com `DEBUG = False` pode mascarar erros durante o desenvolvimento.

### SECRET_KEY hardcoded

A `SECRET_KEY` está hardcoded em `app/settings.py` com o valor padrão do Django (`django-insecure-*`). Em produção, deve ser substituída por uma variável de ambiente.

### db.sqlite3 versionado

O arquivo `.gitignore` tem a linha `#db.sqlite3` comentada, o que significa que o banco SQLite está sendo versionado no git. Isso pode causar conflitos em desenvolvimento colaborativo e expor dados de produção.

## Testes

Apenas o app `genres` possui testes (`genres/tests.py`). Os apps `actors`, `movies`, `reviews` e `authentication` não têm testes.

## Nacionalidades Limitadas

O modelo `Actor` tem `NATIONALITY_CHOICES` hardcoded com apenas 3 opções (`USA`, `BR`, `UK`). Isso limita a escala do sistema e novos países exigem alteração no código fonte e migração.