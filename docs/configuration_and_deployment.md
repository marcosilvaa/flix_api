# Configuração e Deploy

Este documento descreve as configurações principais do projeto e as instruções para deploy em diferentes ambientes.

## Configurações Principais

A configuração principal do projeto está localizada em `app/settings.py`.

### Variáveis Importantes

- **`SECRET_KEY`**: Chave secreta usada para assinatura criptográfica. **Nunca compartilhar ou comitar em repositórios públicos.** Valor padrão é para desenvolvimento apenas.
- **`DEBUG`**: Modo de depuração ativado por padrão (`True`). **DEVE ser definido como `False` em ambiente de produção.**
- **`ALLOWED_HOSTS`**: Lista de hosts/domínios que o Django pode servir. Por padrão está configurado para permitir todos (`['*']`) para desenvolvimento.
- **`DATABASES`**: Configuração do banco de dados. Usa SQLite por padrão para facilitar o desenvolvimento inicial.

## Ambientes

### Desenvolvimento
Para desenvolvimento local, basta seguir as instruções de instalação do guia de desenvolvimento. O banco de dados SQLite é suficiente para testes locais.

### Produção
Para ambiente de produção, recomenda-se:

1. Alterar `DEBUG=False`
2. Configurar `SECRET_KEY` com valor seguro
3. Limitar `ALLOWED_HOSTS` aos domínios específicos
4. Utilizar banco de dados mais robusto (PostgreSQL, MySQL)
5. Configurar servidores web apropriados (nginx, gunicorn, etc.)

### Banco de Dados

O projeto usa SQLite por padrão para facilitar o início rápido. Em produção, recomenda-se migrar para PostgreSQL ou MySQL:

```python
# Exemplo de configuração PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'seu_banco_nome',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Variáveis de Ambiente

Embora o projeto utilize valores padrão, é recomendado usar variáveis de ambiente para configurações sensíveis:

```bash
SECRET_KEY=chave_secreta_segura_aqui
DEBUG=False
DATABASE_URL=postgresql://usuario:senha@localhost/nome_do_banco
ALLOWED_HOSTS=.seu-dominio.com,.outro-dominio.com
```

## Deploy

### Pré-requisitos

Antes do deploy, execute:

```bash
# Coletar arquivos estáticos
python manage.py collectstatic --noinput

# Executar migrações
python manage.py migrate
```

### Servidor de Produção

Para produção, não utilize o servidor de desenvolvimento do Django (`runserver`). Use servidores apropriados como:

- Gunicorn + Nginx
- uWSGI + Nginx
- Serviços de hospedagem especializados em Django

## Segurança

### Recomendações

- Nunca comitar `SECRET_KEY` ou outras credenciais no repositório
- Manter `DEBUG=False` em produção
- Configurar headers de segurança (HTTPS, HSTS, etc.)
- Validar e sanitizar entradas de usuários
- Manter dependências atualizadas