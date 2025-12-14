# Endpoints da API

Este documento lista todos os endpoints disponíveis na API Flix, organizados por módulo.

## Autenticação

### JWT Authentication
```
POST /api/v1/token/          # Obter token de acesso
POST /api/v1/token/refresh/  # Renovar token de acesso
POST /api/v1/token/verify/   # Verificar validade do token
```

## Módulos Disponíveis

### Gêneros (`genres`)
```
GET    /api/v1/genres/        # Listar gêneros
POST   /api/v1/genres/        # Criar gênero
GET    /api/v1/genres/{id}/   # Obter detalhes de um gênero
PUT    /api/v1/genres/{id}/   # Atualizar gênero completo
PATCH  /api/v1/genres/{id}/   # Atualizar parcialmente gênero
DELETE /api/v1/genres/{id}/   # Remover gênero
```

### Atores (`actors`)
```
GET    /api/v1/actors/        # Listar atores
POST   /api/v1/actors/        # Criar ator
GET    /api/v1/actors/{id}/   # Obter detalhes de um ator
PUT    /api/v1/actors/{id}/   # Atualizar ator completo
PATCH  /api/v1/actors/{id}/   # Atualizar parcialmente ator
DELETE /api/v1/actors/{id}/   # Remover ator
```

### Filmes (`movies`)
```
GET    /api/v1/movies/        # Listar filmes
POST   /api/v1/movies/        # Criar filme
GET    /api/v1/movies/{id}/   # Obter detalhes de um filme
PUT    /api/v1/movies/{id}/   # Atualizar filme completo
PATCH  /api/v1/movies/{id}/   # Atualizar parcialmente filme
DELETE /api/v1/movies/{id}/   # Remover filme
```

### Avaliações (`reviews`)
```
GET    /api/v1/reviews/       # Listar avaliações
POST   /api/v1/reviews/       # Criar avaliação
GET    /api/v1/reviews/{id}/  # Obter detalhes de uma avaliação
PUT    /api/v1/reviews/{id}/  # Atualizar avaliação completa
PATCH  /api/v1/reviews/{id}/  # Atualizar parcialmente avaliação
DELETE /api/v1/reviews/{id}/  # Remover avaliação
```

## Permissões

Todos os endpoints (exceto autenticação) exigem autenticação JWT e permissões específicas baseadas no modelo e ação realizada. Veja o documento sobre [Sistema de Permissões](./permissions_system.md) para mais detalhes.