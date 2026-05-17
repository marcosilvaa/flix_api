# Modelos de Dados

Este documento descreve os modelos Django, seus campos, relacionamentos e restrições.

## Diagrama de Relacionamentos

```
Genre ←──────── Movie ────────→ Actor
  (1:N)          │               (N:M)
                 │
                 ↓
               Review
                (1:N)
```

- Um **Genre** tem muitos **Movies** (1:N via `genre` FK).
- Um **Movie** tem muitos **Actors** (N:M via `actors` M2M).
- Um **Movie** tem muitas **Reviews** (1:N via `movie` FK com `related_name='reviews'`).
- Uma **Review** pertence a um **Movie** (N:1 via `movie` FK).

---

## Genre

| Campo | Tipo | Restrições |
|-------|------|-----------|
| `id` | BigAutoField (PK) | Automático |
| `name` | CharField | `max_length=200` |

- `__str__` retorna `self.name`

Archivo: `genres/models.py`

---

## Actor

| Campo | Tipo | Restrições |
|-------|------|-----------|
| `id` | BigAutoField (PK) | Automático |
| `name` | CharField | `max_length=200` |
| `birthdate` | DateField | `blank=True, null=True` |
| `nationality` | CharField | `max_length=100`, `choices=NATIONALITY_CHOICES`, `blank=True, null=True` |

### NATIONALITY_CHOICES

```python
NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BR', 'Brasil'),
    ('UK', 'Reino Unido'),
)
```

> **Nota:** A lista de nacionalidades é limitada a apenas 3 opções codificadas diretamente no modelo. Para expandir, é necessário alterar `actors/models.py`.

- `__str__` retorna `self.name`

Arquivo: `actors/models.py`

---

## Movie

| Campo | Tipo | Restrições |
|-------|------|-----------|
| `id` | BigAutoField (PK) | Automático |
| `title` | CharField | `max_length=500` |
| `genre` | ForeignKey → Genre | `on_delete=PROTECT`, `related_name='movies'` |
| `actors` | ManyToManyField → Actor | `related_name='movies'` |
| `release_date` | DateField | `null=True, blank=True` |
| `resume` | TextField | `null=True, blank=True` |

- `on_delete=PROTECT` em `genre` impede a exclusão de gêneros que possuem filmes associados.
- `__str__` retorna `self.title`

Arquivo: `movies/models.py`

---

## Review

| Campo | Tipo | Restrições |
|-------|------|-----------|
| `id` | BigAutoField (PK) | Automático |
| `movie` | ForeignKey → Movie | `on_delete=PROTECT`, `related_name='reviews'` |
| `stars` | IntegerField | `validators=[MinValueValidator(0), MaxValueValidator(5)]` |
| `comment` | TextField | `null=True, blank=True` |

- `on_delete=PROTECT` em `movie` impede a exclusão de filmes que possuem avaliações.
- Mensagens de validação personalizadas em português: "Avaliação não pode ser inferior a 0 estrelas" / "não pode ser superior a 5 estrelas".
- `__str__` retorna `self.movie.title`

Arquivo: `reviews/models.py`

---

## Relacionamento reverso: reviews em Movie

O modelo `Movie` acessa suas reviews via `related_name='reviews'`:

```python
movie.reviews.all()  # QuerySet de Review
movie.reviews.aggregate(Avg('stars'))  # Média de estrelas
```

Isso é utilizado em `MovieListDetailSerializer.get_rate()` e `MovieStatsView` para calcular a nota média do filme.