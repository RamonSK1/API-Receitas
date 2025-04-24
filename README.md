# API de Receitas

Este projeto é uma API RESTful desenvolvida com **Flask** que permite realizar o CRUD (Criar, Ler, Atualizar e Deletar) de **ingredientes** e **receitas**. Cada receita pode conter múltiplos ingredientes com suas respectivas quantidades e um modo de preparo.

---

## Funcionalidades

- CRUD de ingredientes
- CRUD de receitas
- Associação de ingredientes a receitas com quantidade
- Descrição de modo de preparo por receita

---

## Tecnologias Utilizadas

- Python
- Flask
- Flask-Migrate
- SQLAlchemy
- SQLite (padrão, pode ser substituído por outro banco)

---

## Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/RamonSK1/API-Receitas.git
cd API-Receitas
```

---

### 2. Crie e ative um ambiente virtual (Usei o ambiente virtual do python para evitar problemas e ser mais pratico)

#### Windows (PowerShell):
```bash
python -m venv venv
venv\Scripts\Activate.ps1
```

#### Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure e crie o banco de dados

```bash
flask db init    
flask db migrate -m "Initial migration"
flask db upgrade
```

---

### 5. Rode o servidor

```bash
flask run
```

O servidor estará disponível em:
```
http://127.0.0.1:5000
```

---

## Endpoints principais

### Ingredientes
- `GET /ingredientes` — Lista todos os ingredientes
- `POST /ingredientes` — Cria um novo ingrediente
- `GET /ingredientes/<id>` — Detalha um ingrediente
- `PUT /ingredientes/<id>` — Atualiza um ingrediente
- `DELETE /ingredientes/<id>` — Deleta um ingrediente

### Receitas
- `GET /receitas` — Lista todas as receitas
- `POST /receitas` — Cria uma nova receita
- `GET /receitas/<id>` — Detalha uma receita, com ingredientes
- `PUT /receitas/<id>` — Atualiza uma receita
- `DELETE /receitas/<id>` — Deleta uma receita
- `POST /receitas/<receita_id>/ingredientes` — Adiciona ingredientes à receita


