# Guia de Desenvolvimento

Este documento define as diretrizes e boas práticas para desenvolvimento no projeto Flix API.

## Configuração do Ambiente

### Requisitos
- Python 3.13 ou superior
- uv (gerenciador de pacotes)

### Instalação Inicial
```bash
# Criar ambiente virtual
python -m venv .venv
source .venv/bin/activate  # No Linux/Mac
# ou
.venv\Scripts\activate     # No Windows

# Instalar dependências
uv sync
# ou
pip install -r requirements.txt
```

### Iniciar o Projeto
```bash
# Executar migrações
python manage.py migrate

# Criar superusuário (opcional)
python manage.py createsuperuser

# Iniciar o servidor
python manage.py runserver
```

## Padrões de Codificação

### Estilo de Código
- Utilizar o padrão PEP 8 para formatação de código Python
- Manter linhas com no máximo 88 caracteres
- Utilizar docstrings nos módulos, classes e funções significativos

### Nomenclatura
- Variáveis e funções: `snake_case`
- Classes: `PascalCase`
- Constantes: `UPPER_CASE`
- Arquivos: `snake_case`

## Estrutura de um Novo Módulo

Ao criar um novo módulo funcional no projeto, siga este padrão:

1. Criar pasta com o nome do módulo
2. Implementar os seguintes arquivos:
   - `models.py` - Modelos Django
   - `serializers.py` - Serializers DRF
   - `views.py` - Views DRF
   - `urls.py` - Rotas do módulo
   - `admin.py` - Configurações do admin
   - `tests.py` - Testes unitários

## Práticas Recomendadas

### Models
- Implementar o método `__str__` em todos os modelos
- Utilizar `max_length` adequado para campos CharField
- Usar `blank=True, null=True` quando campos forem opcionais
- Aplicar validações adequadas usando validators do Django

### Serializers
- Utilizar ModelSerializer sempre que possível
- Especificar explicitamente os campos em vez de usar `fields = '__all__'`
- Adicionar validações customizadas quando necessário

### Views
- Utilizar Generic Views do DRF sempre que possível
- Aplicar as permissões padrão (IsAuthenticated e GlobalDefaultPermission)
- Seguir o padrão RESTful para nomenclatura dos endpoints

### URLs
- Organizar endpoints no formato `/api/v1/nome_do_recurso/`
- Utilizar nomes descritivos para as rotas
- Sugerir manter consistência nos padrões de endpoint

## Comandos úteis

```bash
# Rodar testes
python manage.py test

# Criar migrações
python manage.py makemigrations

# Verificar issues de codificação
python -m flake8 .
# ou
ruff check .

# Formatar código automaticamente
black .
# ou
ruff format .
```

## Controle de Versão

- Utilizar commits pequenos e com mensagens descritivas
- Seguir convenção de commits: tipo(scope): descrição curta
  - Exemplo: `feat(movies): adiciona modelo de filme`
- Criar branches com nomes descritivos
- Realizar pull requests para revisão de código