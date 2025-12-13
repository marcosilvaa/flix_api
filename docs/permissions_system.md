# Sistema de Permissões

Este documento explica o sistema de permissões implementado no projeto Flix API, incluindo sua arquitetura e como ele é aplicado em diferentes partes da aplicação.

## Visão Geral

O sistema de permissões é baseado nas permissões padrão do Django, estendidas com uma lógica personalizada para controle refinado de acesso às operações da API. Ele utiliza o conceito de permissões baseadas em modelos (model permissions) com um padrão automático de nomeação.

## Componentes Principais

### GlobalDefaultPermission
Localizado em `app/permissions.py`, esta classe herda de `permissions.BasePermission` do Django REST Framework e implementa a lógica central de verificação de permissões.

Principais responsabilidades:
- Determinar qual permissão é necessária com base no método HTTP
- Verificar se o usuário autenticado possui a permissão necessária
- Interceptar requisições e impedir acesso não autorizado

### Mapeamento de Métodos HTTP para Permissões

O sistema converte automaticamente métodos HTTP em permissões específicas:

| Método HTTP | Ação | Permissão Esperada | Exemplo |
|-------------|------|-------------------|---------|
| GET (lista) | Visualizar | `{app_label}.view_{model_name}` | `movies.view_movie` |
| GET (detalhe) | Visualizar | `{app_label}.view_{model_name}` | `movies.view_movie` |
| POST | Criar | `{app_label}.add_{model_name}` | `movies.add_movie` |
| PUT/PATCH | Atualizar | `{app_label}.change_{model_name}` | `movies.change_movie` |
| DELETE | Remover | `{app_label}.delete_{model_name}` | `movies.delete_movie` |

## Aplicação nas Views

Em cada view genérica do Django REST Framework, o sistema de permissões é aplicado da seguinte forma:

```python
class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
```

Este padrão é consistente em todos os módulos do projeto (actors, genres, movies, reviews).

## Tipos de Permissões

As permissões são compostas pelo nome do app Django (app_label) e pelo nome do modelo (model_name), separados por ponto, seguidos pela ação:

Formato: `{app_label}.{action}_{model_name}`

Exemplos:
- `genres.add_genre` - Permitir adicionar gêneros
- `actors.view_actor` - Permitir visualizar atores
- `movies.change_movie` - Permitir modificar filmes
- `reviews.delete_review` - Permitir remover avaliações

## Gerenciamento de Permissões

### Atribuição a Usuários
As permissões podem ser atribuídas individualmente a usuários através da interface administrativa do Django ou programaticamente:

```python
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from movies.models import Movie

user = User.objects.get(username='usuario_exemplo')
content_type = ContentType.objects.get_for_model(Movie)
permission = Permission.objects.get(
    codename='change_movie',
    content_type=content_type,
)
user.user_permissions.add(permission)
```

### Criação de Grupos
Para facilitar o gerenciamento de permissões, recomenda-se a criação de grupos com conjuntos específicos de permissões:

- Criar grupos como "Administradores", "Editores", "Visualizadores"
- Atribuir as permissões necessárias a cada grupo
- Associar usuários aos grupos apropriados

## Fluxo de Verificação de Permissões

1. Usuário faz requisição autenticada com token JWT
2. View verifica se usuário está autenticado (IsAuthenticated)
3. View chama GlobalDefaultPermission.has_permission()
4. Classe identifica o modelo e o método HTTP da requisição
5. Gera o nome da permissão esperada com base no padrão
6. Verifica se o usuário possui essa permissão
7. Se sim, permite a operação; senão, retorna 403 Forbidden

## Boas Práticas

### Para Desenvolvedores
- Sempre aplicar `GlobalDefaultPermission` nas views que exigem controle de acesso
- Manter consistência na nomenclatura de apps e modelos
- Testar permissões em diferentes níveis de usuário

### Para Administradores
- Planejar cuidadosamente os papéis e responsabilidades
- Utilizar grupos para organizar permissões de forma eficiente
- Revistar periodicamente as permissões atribuídas
- Registrar mudanças de permissões em ambientes de produção