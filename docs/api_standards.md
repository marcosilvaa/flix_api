# Padrões de API

Este documento define os padrões e convenções utilizados na construção da API REST do projeto Flix API.

## Versionamento

A API utiliza versionamento por URL com o formato `/api/v{número}/`.
Exemplo: `/api/v1/movies/`

## Estrutura dos Endpoints

Os endpoints seguem o padrão RESTful:

| Método | Endpoint                      | Ação                    |
|--------|-------------------------------|-------------------------|
| GET    | `/api/v1/resource/`          | Listar recursos         |
| POST   | `/api/v1/resource/`          | Criar recurso           |
| GET    | `/api/v1/resource/{id}/`     | Obter recurso específico|
| PUT    | `/api/v1/resource/{id}/`     | Atualizar recurso       |
| PATCH  | `/api/v1/resource/{id}/`     | Atualizar parcialmente  |
| DELETE | `/api/v1/resource/{id}/`     | Remover recurso         |

## Autenticação

Toda a API requer autenticação via JWT (JSON Web Tokens):

### Obtenção de Token
```
POST /api/v1/authentication/token/
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

### Uso do Token
Enviar o token no cabeçalho de todas as requisições:
```
Authorization: Bearer <seu_token_aqui>
```

### Atualização de Token
```
POST /api/v1/authentication/token/refresh/
{
  "refresh": "<refresh_token_anterior>"
}
```

## Formato das Respostas

### Sucesso (2xx)
```json
{
  "id": 1,
  "nome_campo": "valor"
}
```

### Erros de Validação (400)
```json
{
  "campo": [
    "mensagem de erro"
  ]
}
```

### Erros de Autenticação (401)
```json
{
  "detail": "Erro de autenticação"
}
```

### Erros de Autorização (403)
```json
{
  "detail": "Permissão negada"
}
```

## Padrões de Nomenclatura

### Campos JSON
Utilizar `snake_case` para todos os campos JSON:
```json
{
  "first_name": "João",
  "birth_date": "1990-01-01",
  "nationality": "BR"
}
```

### Nomes de Recursos
Utilizar substantivos no plural para os nomes dos recursos:
- `/api/v1/movies/`
- `/api/v1/actors/`
- `/api/v1/genres/`

## Paginação

Quando aplicável, utilizar paginação padrão do DRF:
```json
{
  "count": 100,
  "next": "/api/v1/resource/?page=2",
  "previous": null,
  "results": [
    // dados dos recursos
  ]
}
```

## Filtragem e Ordenação

Quando implementado, seguir os padrões:
- Filtragem: `?field=valor`
- Ordenação: `?ordering=campo` ou `?ordering=-campo` (descendente)

## Tratamento de Erros

A API deve retornar mensagens de erro claras e úteis para auxiliar o desenvolvedor:
- Erros de validação devem especificar quais campos estão incorretos
- Erros de negócio devem conter explicações detalhadas
- Evitar expor detalhes internos do sistema em mensagens de erro