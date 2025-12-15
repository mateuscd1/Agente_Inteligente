-- =========================
-- TABELA DE USUÁRIOS
-- =========================
CREATE TABLE usuario (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(150) NOT NULL UNIQUE,
    email VARCHAR(150) NOT NULL,
    password VARCHAR(255) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT 1
);

-- =========================
-- TABELA PERFIL TÉCNICO
-- =========================
CREATE TABLE perfil_tecnico (
    id_perfil INTEGER PRIMARY KEY AUTOINCREMENT,
    cpf VARCHAR(14) NOT NULL UNIQUE,
    aprovado BOOLEAN NOT NULL DEFAULT 0,
    id_usuario INTEGER NOT NULL,
    FOREIGN KEY (id_usuario)
        REFERENCES usuario (id_usuario)
        ON DELETE CASCADE
);

-- =========================
-- TABELA DOCUMENTO
-- =========================
CREATE TABLE documento (
    id_documento INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(255) NOT NULL,
    arquivo VARCHAR(255) NOT NULL,
    texto_extraido TEXT,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    id_usuario INTEGER NOT NULL,
    FOREIGN KEY (id_usuario)
        REFERENCES usuario (id_usuario)
        ON DELETE CASCADE
);
