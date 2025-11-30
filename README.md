# Sistema de Repositório Institucional com um Agente Inteligente

A Pró-Reitoria de Pesquisa e Pós-Graduação (PPG) da UEMA (Universidade Estadual do Maranhão) necessita de um agente inteligente para gerenciar, classificar e consultar automaticamente informações e documentos institucionais relacionados à pesquisa e pós-graduação.
 Atualmente, documentos como editais, relatórios, dissertações, projetos e produções científicas são gerenciados manualmente, o que torna o processo lento, redundante e suscetível a erros. Este projeto tem como objetivo:
 - Organização automática de documentos por: tipo, área e programa.

 - Consultas semânticas com linguagem natural ("Mostrar editais de bolsas 2025")

 - Geração automática de relatórios e sumários técnicos (usando prompts)

 - Integração com modelos PLN (Processamento de Linguagem Natural) para análise textual e sumarização

# Sistema

A princípio o sistema será desenvolvido em Python, com uso de banco de dados PostgreSQL, Django para integração de interface Web  e integração com modelos de linguagem (transformers) para consulta semântica e geração de documentação. Utiliza GitHub/GitLab para versionamento e automação CI/CD.

# Página estrutura

![Descrição da Imagem](assets/pagina_inicial_prototipo.png)

# Modelagem Conceitual 

Entidades principais:

- Documento (id, tipo, título, descrição, arquivo, setor_id)


- Programa (id, nome, nível, área, coordenador)


- UsuárioPPG (id, nome, cpf, identificador , email, senha)


- FluxoAprovacao (id, etapa, responsável, status)


- ResumoIA (id, documento_id, resumo_textual, tópicos_extraídos)


- EmbeddingVetorial (id, documento_id, vetor_semântico)

#
# Estrutura inicial

```
├── 📁 core
│   ├── 📁 management
│   │   ├── 📁 commands
│   │   │   └── 🐍 __init__.py
│   │   └── 🐍 __init__.py
│   ├── 📁 migrations
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
│   ├── 🐍 __init__.py
│   ├── 🐍 admin.py
│   ├── 🐍 apps.py
│   ├── 🐍 models.py
│   ├── 🐍 tests.py
│   ├── 🐍 urls.py
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
├── 🖼️ Página_Inicial_Desenvolvimento.png
├── 📝 README.md
├── 🐍 manage.py
└── 📄 requirements.txt
```

