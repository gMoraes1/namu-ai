# 🧠 AI Wellness Recommendation API

API backend desenvolvida com **FastAPI + PostgreSQL + Ollama (LLM
local)** para geração inteligente de recomendações de bem-estar
personalizadas com base no perfil do usuário.

Projeto desenvolvido como parte de teste técnico para vaga de
Desenvolvedor Backend Python com foco em IA.

------------------------------------------------------------------------

# 🚀 Tecnologias Utilizadas

-   Python 3.11+
-   FastAPI
-   PostgreSQL
-   SQLAlchemy (ORM)
-   SQL Raw (queries analíticas)
-   Pydantic
-   Poetry (gerenciamento de dependências)
-   Ollama (LLM local -- Llama3)
-   Pytest
-   Pytest-asyncio

------------------------------------------------------------------------

# 🏗 Arquitetura do Projeto

app/
├── main.py
├── database.py
├── core/
├── models/
├── schemas/
├── crud/
├── routers/
├── service/
└── utils/

tests/
├── test_users.py

Arquitetura modular seguindo boas práticas de backend.

------------------------------------------------------------------------

# 🧠 Integração com IA

Fluxo:

1.  Usuário envia contexto
2.  Sistema consulta perfil no banco
3.  Prompt estruturado é construído
4.  LLM gera resposta em formato JSON
5.  Resposta é validada via Pydantic
6.  Resultado é persistido no banco

Formato esperado da LLM:

{ "activities": \[ { "name": "...", "description": "...", "duration":
"...", "category": "..." } \], "reasoning": "...", "precautions": "..."
}

------------------------------------------------------------------------

# 🛠 Como Rodar o Projeto

## 1️⃣ Clonar o repositório

git clone https://github.com/gMoraes1/namu-ai cd namu-ai

## 2️⃣ Instalar dependências com Poetry

pip install poetry poetry install poetry shell

## 3️⃣ Configurar variáveis de ambiente

Criar arquivo .env:

DB_HOST=localhost
DB_PORT=5432
DB_USER=namu
DB_PASSWORD=namu123
DB_NAME=namu_ai

# LLM Configuration 
LLM_MODEL=llama3
OLLAMA_BASE_URL=http://localhost:11434

## 4️⃣ Rodar PostgreSQL via Docker Compose

docker compose up -d

## 5️⃣ Instalar e rodar ollama

Linux : curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3 ollama run llama3

## 6️⃣ Rodar API

uvicorn app.main:app --reload

Documentação automática: http://localhost:8000/docs

------------------------------------------------------------------------

# 📌 Endpoints

## Usuários

POST /users\
GET /users/{user_id}\
GET /users/{user_id}/recommendations\
GET /users/{user_id}/stats

## Recomendações

POST /recommendations\
POST /recommendations/{recommendation_id}/feedback

------------------------------------------------------------------------

# 🔒 Tratamento de Erros

-   404 para recursos inexistentes
-   500 para falha no parsing da LLM
-   Validação via Pydantic
-   SQL raw com parâmetros nomeados (proteção contra SQL Injection)

------------------------------------------------------------------------

# 📊 Diferenciais

✔ Integração real com LLM local\
✔ Prompt estruturado\
✔ JSONB no PostgreSQL\
✔ SQL raw com JOIN e agregações\
✔ Arquitetura modular\
✔ Swagger automático
✔ Testes automatizados com Pytest

------------------------------------------------------------------------

🔮 Próximas Melhorias
- Implementação completa de testes automatizados para todas as rotas
- Separação de banco de dados específico para ambiente de testes
- Containerização completa da aplicação (API + DB + LLM)

------------------------------------------------------------------------

# 👨‍💻 Autor

Gustavo Moraes
