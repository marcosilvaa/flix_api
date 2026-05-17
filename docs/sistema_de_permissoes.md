# Sistema de Permissões

O Flix API utiliza permissões baseadas em modelos Django, com mapeamento automático de métodos HTTP para ações de permissão.

## Arquitetura

O sistema de permissões é implementado em duas camadas em cada view:

```python
permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
```

1. **`IsAuthenticated`**: Garante que o usuário está autenticado via JWT.
2. **`GlobalDefaultPermission`** (`app/permissions.py`): Verifica se o usuário possui a permissão de modelo correspondente à ação.

## Mapeamento HTTP → Permissão

O `GlobalDefaultPermission` converte automaticamente o método HTTP em uma permissão Django:

| Método HTTP | Sufixo | Exemplo |
|-------------|--------|---------|
| GET, OPTIONS, HEAD | `view` | `movies.view_movie` |
| POST | `add` | `movies.add_movie` |
| PUT, PATCH | `change` | `movies.change_movie` |
| DELETE | `delete` | `movies.delete_movie` |

A permissão é construída no formato `{app_label}.{action}_{model_name}`, onde `app_label` e `model_name` são obtidos do `queryset.model._meta` da view.

## Como Funciona

```python
# app/permissions.py — lógica simplificada
class GlobalDefaultPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        model_name = view.queryset.model._meta.model_name
        app_label = view.queryset.model._meta.app_label
        action = self.__get_action_sufix(request.method)
        permission = f'{app_label}.{action}_{model_name}'
        return request.user.has_perm(permission)
```

Se a view não possuir `queryset`, `has_permission` retorna `False` (o bloco `except AttributeError` retorna `None`, que é falsy).

## Gerenciamento de Permissões

As permissões são gerenciadas pelo sistema padrão do Django:

- **Superusuário**: Possui todas as permissões automaticamente.
- **Admin interface**: Atribuir permissões individualmente ou via grupos em `/admin/`.
- **Programaticamente**:

```python
from django.contrib.auth.models import User, Permission
user = User.objects.get(username='usuario')
permission = Permission.objects.get(codename='view_movie')
user.user_permissions.add(permission)
```

## Exceção: GenrePermissionClass

O arquivo `genres/permissions.py` contém `GenrePermissionClass`, que implementa o mesmo mapeamento manualmente com `if/elif`. **Essa classe não é utilizada** nas views de gêneros, que usam `GlobalDefaultPermission` em vez dela. É um artefato de código morto.

## Permissões por Modelo

| Modelo | Permissões Disponíveis |
|--------|----------------------|
| Genre | `genres.view_genre`, `genres.add_genre`, `genres.change_genre`, `genres.delete_genre` |
| Actor | `actors.view_actor`, `actors.add_actor`, `actors.change_actor`, `actors.delete_actor` |
| Movie | `movies.view_movie`, `movies.add_movie`, `movies.change_movie`, `movies.delete_movie` |
| Review | `reviews.view_review`, `reviews.add_review`, `reviews.change_review`, `reviews.delete_review` |

## View Especial: MovieStatsView

`MovieStatsView` herda de `views.APIView` (não de `generics.*`), mas define `queryset = Movie.objects.all()` como atributo de classe. Isso é necessário para que `GlobalDefaultPermission` possa inferir o modelo e a permissão (`movies.view_movie`), já que a classe busca `view.queryset.model` dinamicamente.