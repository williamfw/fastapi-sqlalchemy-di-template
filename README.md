# FastAPI + SQLAlchemy + Dependency Injection Template

Olá, como vai?
Ao longo da minha carreira no desenvolvimento de software, vi e experimentei diversos design patterns muito bons e, um dos que mais aprecio é o Dependency Injection (DI).
O DI já é bem difundido em .NET e Springboot por exemplo, porém no Python notei que, apesar de terem vários framework de DI, tive uma dificuldade de encontrar um framework que se assemelhasse aos padrôes definidos pelo .NET por exemplo.
Então, investi um tempo e criei este repositório pra usar nos meus projetos Python e compartilhar com vocês! Este repositório fornece um template básico para criar uma aplicação FastAPI com [SQLAlchemy](https://www.sqlalchemy.org/) (ORM) e [Inject](https://github.com/ivankorobkov/python-inject) (Dependency Injection). 

Vamos lá!

## Índice

- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Rodando o Projeto](#rodando-o-projeto)
- [Rodando Testes](#rodando-testes)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Pré-requisitos

Antes de começar, certifique-se de ter as seguintes ferramentas instaladas:

- [Python 3.12+](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)
- [Docker](https://docs.docker.com/get-docker/) (usa Windows? então leia esse [tutorial](https://github.com/codeedu/wsl2-docker-quickstart))
- [Docker Compose](https://docs.docker.com/compose/)

## Instalação

1. **Clone o Repositório**:

   ```bash
   git clone https://github.com/williamfw/fastapi-sqlalchemy-di-template.git
   cd fastapi-sqlalchemy-di-template
   ```

2. **Instale as Dependências**:

   Este projeto usa `Poetry` para gerenciar as dependências. Instale-as com:

   ```bash
   poetry install
   ```

3. **Ative o Ambiente Virtual**:

   Ative o ambiente virtual criado pelo `Poetry`:

   ```bash
   poetry shell
   ```

## Configuração

### Variáveis de Ambiente

Este projeto usa variáveis de ambiente para configurar o banco de dados. Você pode alterar o arquivo `.env` na raiz do projeto e definir as variáveis de ambiente necessárias.

### Configuração do Banco de Dados

Por padrão, o projeto está configurado para usar um banco de dados PostgreSQL. Para iniciar o serviço e criar a base, rode o seguinte comando:

```bash
docker-compose up -d
```

Isso iniciará um contêiner Docker com PostgreSQL usando as configurações definidas em `docker-compose.yml`.

Caso prefira rodar o PostgreSQL localmente ou em outro ambiente, configure a variável `SQLALCHEMY_DATABASE_URL` no arquivo `.env` para apontar para sua instância do banco de dados.

## Rodando o Projeto

Após configurar o projeto, acesse o diretorio backend no terminal e inicie o servidor:

```bash
cd backend
fastapi dev main.py
```

Esse comando inicia o servidor FastAPI em modo de desenvolvimento, com hot-reloading ativado. O servidor estará disponível em `http://127.0.0.1:8000`.

## Estrutura do Projeto

```plaintext
fastapi-sqlalchemy-di-template/
.
├── backend
│   ├── alembic
│   │   ├── env.py
│   │   ├── README
│   │   ├── script.py.mako
│   ├── alembic.ini
│   ├── api
│   │   ├── controllers
│   │   │   ├── customers
│   │   │   │   ├── customer_controller.py
│   │   │   │   ├── job_controller.py
│   ├── domain
│   │   ├── database
│   │   │   ├── models
│   │   │   │   ├── customer_model.py
│   │   │   │   ├── job_model.py
│   │   │   └── repositories
│   │   │       ├── customer_repository.py
│   │   │       ├── job_repository.py
│   │   ├── dto
│   │   │   ├── customer_dto.py
│   │   │   ├── job_dto.py
│   │   ├── interfaces
│   │   │   ├── repositories
│   │   │   │   ├── i_customer_repository.py
│   │   │   │   ├── i_job_repository.py
│   │   │   └── services
│   │   │       ├── i_customer_service.py
│   │   │       ├── i_job_service.py
│   │   └── services
│   │       ├── customer_service.py
│   │       ├── job_service.py
│   ├── infrastructure
│   │   ├── database
│   │   │   ├── database_session_manager.py
│   │   ├── dto
│   │   │   ├── base_dto.py
│   │   ├── ioc
│   │   │   ├── ioc.py
│   │   ├── model
│   │   │   ├── base_model.py
│   │   ├── repository
│   │   │   ├── base_repository.py
│   │   └── settings
│   │       └── settings.py
│   ├── main.py
│   ├── poetry.lock
│   ├── pyproject.toml
│   ├── README.md
│   └── tests
└── docker-compose.yml```

- `backend/api`: Endpoints da aplicação.
- `backend/domain`: Camada com a lógica da aplicação.
- `backend/infrastructure`: Camada com configurações da aplicação.
- `backend/main.py`: Ponto de entrada para a aplicação FastAPI.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

---
