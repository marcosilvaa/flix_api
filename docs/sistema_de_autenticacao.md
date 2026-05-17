# Sistema de Autenticação

A autenticação do Flix API é baseada em JWT (JSON Web Tokens) usando a biblioteca `djangorestframework-simplejwt`.

## Configuração

Definida em `app/settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
}
```

- **Token de acesso**: válido por 1 dia.
- **Token de refresh**: válido por 7 dias.
- JWT é a autenticação padrão para **todos** os endpoints da API.

## Endpoints

| Ação | Método | Endpoint |
|------|--------|----------|
| Obter token | POST | `/api/v1/authentication/token/` |
| Renovar token | POST | `/api/v1/authentication/token/refresh/` |
| Verificar token | POST | `/api/v1/authentication/token/verify/` |

Esses endpoints são os únicos que **não exigem** autenticação prévia (são públicos).

## Fluxo de Autenticação

1. **Obter tokens**:Enviar `username` e `password` para `/api/v1/authentication/token/`. Receber `access` e `refresh`.
2. **Usar token**: Incluir o header `Authorization: Bearer <access_token>` em todas as requisições subsequentes.
3. **Renovar acesso**: Quando o access token expirar (após 1 dia), enviar o `refresh` token para `/api/v1/authentication/token/refresh/` para obter um novo access token.

## Estrutura do App `authentication/`

O app `authentication` é minimalista — contém apenas:

- `urls.py`: Registra as 3 rotas JWT usando views prontas do SimpleJWT (`TokenObtainPairView`, `TokenRefreshView`, `TokenVerifyView`).
- `apps.py`: Configuração do app (`AuthenticationConfig`).
- Não possui modelos, views ou serializers próprios.

O app `authentication` está registrado em `INSTALLED_APPS` e suas URLs são incluídas em `app/urls.py` sob o prefixo `/api/v1/`.

## Código de Erro

| Status | Cenário |
|--------|---------|
| 401 | Token ausente, inválido ou expirado |
| 403 | Token válido mas sem permissão para a ação |