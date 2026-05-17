# Padrões e Convenções

Este documento descreve os padrões de código e convenções adotados no projeto.

## Estrutura de um App (Módulo)

Cada app de domínio (`actors`, `genres`, `movies`, `reviews`) segue a mesma estrutura:

```
app_name/
├── models.py        # Modelos Django
├── serializers.py   # Serializers DRF
├── views.py         # Views DRF (generic views)
├── urls.py          # Rotas do módulo
├── admin.py         # Registro no Django Admin
├── apps.py          # Config do app
├── __init__.py
└── migrations/      # Migrações do banco
```

## Padrão de Views

Todas as views seguem o padrão de **generic views** do DRF:

- **CreateListView** (`ListCreateAPIView`): atende `GET` (listar) e `POST` (criar).
- **RetrieveUpdateDestroyView** (`RetrieveUpdateDestroyAPIView`): atende `GET` (detalhe), `PUT`/`PATCH` (atualizar) e `DELETE` (remover).

Permissões aplicadas uniformemente:

```python
permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
```

## Padrão de Serialização Dupla (Movies)

O módulo `movies` usa um padrão diferente dos demais: `get_serializer_class()` retorna serializers distintos conforme o método HTTP:

- **GET**: `MovieListDetailSerializer` — expande `genre` e `actors` como objetos aninhados e inclui o campo calculado `rate`.
- **POST/PUT/PATCH**: `MovieModelSerializer` — aceita IDs em `genre` e `actors`.

Os demais apps (`actors`, `genres`, `reviews`) usam um único serializer para leitura e escrita.

## Padrão de URLs

Todos os endpoints são montados sob `/api/v1/` com o nome do recurso no plural:

```
/api/v1/{recurso}/           → List/Create
/api/v1/{recurso}/{id}/     → Retrieve/Update/Destroy
```

Exceções:
- `/api/v1/movies/stats/` — endpoint customizado de estatísticas.
- `/api/v1/movies/{id}` (sem barra final) e `/api/v1/reviews/{id}` (sem barra final) — diferença inconsistente de trailing slash em relação a `/api/v1/genres/{id}/` e `/api/v1/actors/{id}/`.

## Nomenclatura

- **Variáveis e funções**: `snake_case`
- **Classes**: `PascalCase`
- **Constantes**: `UPPER_CASE`
- **Campos JSON**: `snake_case`
- **Recursos de API**: substantivos no plural (`/actors/`, `/movies/`, etc.)

## Serializers

### Convenção geral
- Uso de `ModelSerializer` com `fields = '__all__'` na maioria dos apps.

### Exceções por app

| App | Serializer | Observação |
|-----|-----------|------------|
| genres | `GenreSerializer` | `fields = ['id', 'name']` (explícito, comentou `__all__`) |
| actors | `ActorSerializer` | `fields = '__all__'` |
| movies | `MovieSerializer` | Serializer manual (não é ModelSerializer), campos explícitos |
| movies | `MovieModelSerializer` | `fields = '__all__'`, com validações customizadas |
| movies | `MovieListDetailSerializer` | Expandi genres/actors como objetos aninhados + campo `rate` |
| movies | `MovieStatsSerializer` | Serializer manual para endpoint de estatísticas |
| reviews | `ReviewSerializers` | `fields = '__all__'` (nome no plural — ver problemas conhecidos) |

## Admin

Todos os modelos estão registrados no Django Admin com `list_display` customizado:

| Modelo | `list_display` |
|--------|---------------|
| Actor | `id, name, birthdate, nationality` |
| Genre | `id, name` |
| Movie | `id, title, release_date, resume` |
| Review | `id, movie, stars, comment` |

## Validações Customizadas

No `MovieModelSerializer`:

- `validate_release_date`: rejeita anos anteriores a 1900 (mensagem diz "1990" — ver problemas conhecidos).
- `validate_resume`: rejeita resumos com mais de 500 caracteres (mensagem diz "200" — ver problemas conhecidos).

No modelo `Review`:

- `stars`: `MinValueValidator(0)` e `MaxValueValidator(5)` com mensagens em português.

## Comando de Gerenciamento Customizado

```bash
python manage.py import_actors <arquivo.csv>
```

Importa atores a partir de um arquivo CSV com colunas `name`, `birthday` (formato `YYYY-MM-DD`) e `nationality`. O arquivo `actors.csv` na raiz do projeto serve como exemplo.