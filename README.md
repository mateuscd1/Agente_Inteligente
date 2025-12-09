# 🧠 Agente Inteligente — PPG UEMA  
Sistema Web para suporte às atividades do Programa de Pós-Graduação da UEMA.

O projeto tem como objetivo auxiliar estudantes e pesquisadores na busca de informações, envio de documentos e interação com um **agente inteligente** (IA) baseado em modelos de linguagem (LLMs), utilizando RAG (Retrieval-Augmented Generation).

---

# Estrutura Página

- Página Inicial

![Descrição da Imagem](assets/pagina_inicial_prototipo.png)

- Página de conversa com Agente Inteligente

![Descrição da Imagem](assets/pagina_conversa.png)

## 🚀 Funcionalidades Atuais

### 👤 **1. Registro de Técnico PPG**
- Cadastro através de formulário com validação (nome, CPF, identificador, e-mail e senha).
- CPF é utilizado como **username** (somente dígitos).
- Usuários recém-registrados ficam com:
  - `is_active = False`
  - pertencentes ao grupo `Pending`
- Somente administradores podem aprovar contas.

---

### 🔐 **2. Login & Logout**
- Login realizado via CPF + senha.
- Após login bem-sucedido, o sistema exibe:
  - saudação com o nome do usuário
  - acesso restrito a recursos especiais (ex.: upload)
  - botão “Sair”
- Logout implementado com comportamento limpo e funcional.

---

### 🗂️ **3. Controle de Acesso por Grupos**
Grupos utilizados:
- **Pending** → Usuários aguardando aprovação
- **Uploader** → Técnicos aprovados pelo administrador
- **Leitor** → Futuro grupo para usuários sem permissão de upload

A aprovação é feita no Django Admin:
- marca `is_active=True`
- adiciona ao grupo **Uploader**

Apenas usuários Uploader conseguem acessar `/upload/`.

---

### 💬 **4. Chat com o Agente Inteligente (interface pronta)**
- Interface completa do chat já está implementada.
- Backend ainda será conectado ao módulo de IA.

---

### 📄 **5. Design Responsivo e Integrado**
- Página inicial, login, registro e chat estilizados com CSS puro.
- Layout limpo, intuitivo e pronto para apresentação.

---

## 🧩 Tecnologias Utilizadas

| Camada | Tecnologia |
|--------|------------|
| Backend | Django 5.x (Python) |
| Banco de Dados | SQLite (desenvolvimento) |
| Front-end | HTML + CSS + JavaScript |
| Autenticação | Django Auth + Groups |
| IA (futuro) | HuggingFace Transformers + RAG |
| Versionamento | Git & GitHub |

---

## 🔧 Instalação e Execução do Projeto

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/mateuscd1/Agente_Inteligente.git
cd Agente_Inteligente
```

```
python -m venv venv

venv/Scripts/activate     # Windows

source venv/bin/activate  # Linux/Mac

pip install -r requirements.txt
```
```
pip install -r requirements.txt
```
```
python manage.py migrate
```
```
python manage.py createsuperuser
```
```
python manage.py runserver
```

## 🔐 Fluxo Completo do Técnico PPG


**1. Usuário acessa /register/ e envia seus dados.**

**2. O sistema cria o usuário com:**
- username = CPF (somente dígitos)

- is_active = False

- grupo = Pending

**3. Administrador acessa /admin/, vai em Users:**

- ativa o usuário (is_active = True)

- o adiciona ao grupo Uploader

**4. Técnico faz login normalmente e obtém acesso à área restrita (ex.: /upload/).**

## 🧱 Estrutura do Projeto

```
├── 📁 assets
│   ├── 🖼️ Página_Inicial_Desenvolvimento.png
│   ├── 🖼️ pagina_conversa.png
│   └── 🖼️ pagina_inicial_prototipo.png
├── 📁 core
│   ├── 📁 management
│   │   ├── 📁 commands
│   │   │   ├── 🐍 __init__.py
│   │   │   └── 🐍 create_groups.py
│   │   └── 🐍 __init__.py
│   ├── 📁 migrations
│   │   ├── 🐍 0001_initial.py
│   │   └── 🐍 __init__.py
│   ├── 📁 templates
│   │   └── 📁 core
│   │       ├── 🌐 base.html
│   │       ├── 🌐 chat.html
│   │       ├── 🌐 document_detail.html
│   │       ├── 🌐 home.html
│   │       ├── 🌐 login.html
│   │       ├── 🌐 register.html
│   │       ├── 🌐 resumo.html
│   │       ├── 🌐 search.html
│   │       └── 🌐 upload.html
│   ├── 📁 templatetags
│   ├── 🐍 __init__.py
│   ├── 🐍 admin.py
│   ├── 🐍 apps.py
│   ├── 🐍 forms.py
│   ├── 🐍 models.py
│   ├── 🐍 tests.py
│   ├── 🐍 urls.py
│   ├── 🐍 utils.py
│   └── 🐍 views.py
├── 📁 repositorio_ppg
│   ├── 🐍 __init__.py
│   ├── 🐍 asgi.py
│   ├── 🐍 settings.py
│   ├── 🐍 urls.py
│   └── 🐍 wsgi.py
├── 📁 static
│   ├── 📁 css
│   │   └── 🎨 style.css
│   ├── 📁 img
│   │   └── 🖼️ ppguema.png
│   └── 📁 js
│       └── 📄 chat.js
├── ⚙️ .env.example
├── ⚙️ .gitignore
├── 📝 README.md
├── 🐍 manage.py
└── 📄 requirements.txt
```
## 🧑‍💻 Contribuição

Contribuições são bem-vindas!

- 1 - Faça um fork do projeto

- 2 - Crie uma branch (git checkout -b feature-nome)

- 3 - Commit e push

- 4 - Abra um Pull Request

## 📄 Licença

Projeto desenvolvido para fins acadêmicos (UEMA — Programa de Pós-Graduação).

## 🧠 Autor

João Mateus Dutra — Aluno de graduação de Engenharia de Computação da UEMA | Desenvolvedor do Agente Inteligente – PPG UEMA.