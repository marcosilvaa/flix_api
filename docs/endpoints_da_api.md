# Endpoints da API

Todos os endpoints estão sob o prefixo `/api/v1/` e exigem autenticação JWT via header `Authorization: Bearer <token>`. Estes endpoints alimentam o dashboard **Flix App** ([github.com/marcosilvaa/flix_app](https://github.com/marcosilvaa/flix_app)).

## Autenticação

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/api/v1/authentication/token/` | Obter par de tokens (access + refresh) |
| POST | `/api/v1/authentication/token/refresh/` | Renovar token de acesso |
| POST | `/api/v1/authentication/token/verify/` | Verificar validade do token |

### Obter token

```json
// POST /api/v1/authentication/token/
// Request body:
{ "username": "seu_usuario", "password": "sua_senha" }

// Response (200):
{ "access": "eyJ...", "refresh": "djK..." }
```

---

## Gêneros

| Método | Endpoint | Ação | Permissão |
|--------|----------|------|-----------|
| GET | `/api/v1/genres/` | Listar gêneros | `genres.view_genre` |
| POST | `/api/v1/genres/` | Criar gênero | `genres.add_genre` |
| GET | `/api/v1/genres/{id}/` | Detalhe do gênero | `genres.view_genre` |
| PUT | `/api/v1/genres/{id}/` | Atualizar gênero | `genres.change_genre` |
| PATCH | `/api/v1/genres/{id}/` | Atualizar parcialmente | `genres.change_genre` |
| DELETE | `/api/v1/genres/{id}/` | Remover gênero | `genres.delete_genre` |

```json
// POST /api/v1/genres/
{ "name": "Ação" }

// Response (201):
{ "id": 1, "name": "Ação" }
```

---

## Atores

| Método | Endpoint | Ação | Permissão |
|--------|----------|------|-----------|
| GET | `/api/v1/actors/` | Listar atores | `actors.view_actor` |
| POST | `/api/v1/actors/` | Criar ator | `actors.add_actor` |
| GET | `/api/v1/actors/{id}/` | Detalhe do ator | `actors.view_actor` |
| PUT | `/api/v1/actors/{id}/` | Atualizar ator | `actors.change_actor` |
| PATCH | `/api/v1/actors/{id}/` | Atualizar parcialmente | `actors.change_actor` |
| DELETE | `/api/v1/actors/{id}/` | Remover ator | `actors.delete_actor` |

```json
// POST /api/v1/actors/
{ "name": "Location", "birthdate": "1949-07-08", "nationality": "USA" }
```

---

## Filmes

| Método | Endpoint | Ação | Permissão |
|--------|----------|------|-----------|
| GET | `/api/v1/movies/` | Listar filmes | `movies.view_movie` |
| POST | `/api/v1/movies/` | Criar filme | `movies.add_movie` |
| GET | `/api/v1/movies/{id}` | Detalhe do filme | `movies.view_movie` |
| PUT | `/api/v1/movies/{id}` | Atualizar filme | `movies.change_movie` |
| PATCH | `/api/v1/movies/{id}` | Atualizar parcialmente | `movies.change_movie` |
| DELETE | `/api/v1/movies/{id}` | Remover filme | `movies.delete_movie` |
| GET | `/api/v1/movies/stats/` | Estatísticas de filmes | `movies.view_movie` |

### Padrão de serialização dupla

Os endpoints de filmes usam **serializers diferentes** para leitura e escrita:

- **GET**: usa `MovieListDetailSerializer`, que expande `genre` e `actors` como objetos completos e inclui o campo calculado `rate` (média de estrelas das reviews).
- **POST/PUT/PATCH**: usa `MovieModelSerializer`, que aceita IDs para `genre` e `actors`.

```json
// GET /api/v1/movies/1
{
  "id": 1,
  "title": "Inception",
  "genre": { "id": 1, "name": "Sci-Fi" },
  "actors": [{ "id": 1, "name": "Leonardo DiCaprio", ... }],
  "release_date": "2010-07-16",
  "rate": 4.5,
  "resume": "A thief who steals corporate secrets..."
}

// POST /api/v1/movies/
{ "title": "Inception", "genre": 1, "actors": [1], "release_date": "2010-07-16", "resume": "..." }
```

### Endpoint de estatísticas

`GET /api/v1/movies/stats/` retorna:

```json
{
  "total_movies": 10,
  "movies_by_genre": [ { "genre__name": "Sci-Fi", "count": 3 } ],
  "total_reviews": 25,
  "average_stars": 4.2
}
```

> **Nota:** A URL de detalhe do filme usa `/movies/<int:pk>` (sem barra final), enquanto a de gêneros e atores usam `/genres/<int:pk>/` (com barra final). Ver [Problemas Conhecidos](problemas_conhecidos.md).

---

## Avaliações

| Método | Endpoint | Ação | Permissão |
|--------|----------|------|-----------|
| GET | `/api/v1/reviews/` | Listar avaliações | `reviews.view_review` |
| POST | `/api/v1/reviews/` | Criar avaliação | `reviews.add_review` |
| GET | `/api/v1/reviews/{id}` | Detalhe da avaliação | `reviews.view_review` |
| PUT | `/api/v1/reviews/{id}` | Atualizar avaliação | `reviews.change_review` |
| PATCH | `/api/v1/reviews/{id}` | Atualizar parcialmente | `reviews.change_review` |
| DELETE | `/api/v1/reviews/{id}` | Remover avaliação | `reviews.delete_review` |

```json
// POST /api/v1/reviews/
{ "movie": 1, "stars": 5, "comment": "Excelente filme!" }
```

> **Nota:** A URL de detalhe usa `/reviews/<int:pk>` (sem barra final).