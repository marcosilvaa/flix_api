# Sistema de Autenticação

Este documento descreve o sistema de autenticação implementado no projeto Flix API, incluindo como obter e usar tokens JWT.

## Visão Geral

O sistema de autenticação é baseado em JWT (JSON Web Tokens) utilizando a biblioteca `djangorestframework-simplejwt`. Todos os endpoints da API, exceto os de autenticação, exigem um token JWT válido para acesso.

## Funcionamento

O processo de autenticação envolve três etapas principais:

1. **Obtenção de Token**: O usuário fornece credenciais válidas (usuário e senha) para obter um token de acesso.
2. **Uso do Token**: O token é enviado em cada requisição subsequente no cabeçalho `Authorization`.
3. **Renovação de Token**: Tokens de acesso têm tempo limitado e precisam ser renovados periodicamente.

## Endpoints de Autenticação

### Obter Token
```
POST /api/v1/authentication/token/
```

**Corpo da Requisição:**
```json
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

**Resposta de Sucesso (200 OK):**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh": "djKnTxb9c4MV77t9bfJmtpRTnu7euKpwr..."
}
```

### Renovar Token de Acesso
```
POST /api/v1/authentication/token/refresh/
```

**Corpo da Requisição:**
```json
{
  "refresh": "seu_refresh_token_aqui"
}
```

**Resposta de Sucesso (200 OK):**
```json
{
  "access": "novo_token_de_acesso_aqui..."
}
```

### Verificar Token
```
POST /api/v1/authentication/token/verify/
```

**Corpo da Requisição:**
```json
{
  "token": "seu_token_para_verificar"
}
```

**Resposta de Sucesso (200 OK):**
```json
{
  "token": "seu_token_para_verificar"
}
```

## Configurações de Token

### Tempo de Vida
- **Token de Acesso**: 1 dia
- **Token de Refresh**: 7 dias

Essas configurações podem ser alteradas no arquivo `settings.py` na seção `SIMPLE_JWT`.

## Uso do Token em Requisições

Após obter um token de acesso, ele deve ser incluído no cabeçalho de todas as requisições protegidas:

```
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
```

## Erros Comuns de Autenticação

- **401 Unauthorized**: Token ausente, inválido ou expirado
- **403 Forbidden**: Token válido mas usuário sem permissão para a ação
- **400 Bad Request**: Credenciais inválidas ou formato incorreto

## Boas Práticas

- Armazenar tokens de forma segura no cliente
- Implementar renovação automática de tokens antes da expiração
- Tratar erros de autenticação de forma apropriada
- Nunca expor tokens em URLs ou logs