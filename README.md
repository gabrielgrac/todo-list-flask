# 📋 TODO LIST — Versão Web com Flask

Gestor de tarefas acessível no browser — PC e telemóvel — construído com Flask (Python) e HTML/CSS/JS puro, sem base de dados.

![Python](https://img.shields.io/badge/linguagem-Python%203-blue?logo=python)
![Flask](https://img.shields.io/badge/framework-Flask-black?logo=flask)
![Plataformas](https://img.shields.io/badge/acesso-Browser%20%7C%20Mobile-green)
![Licença](https://img.shields.io/badge/licen%C3%A7a-MIT-lightgrey)

---

## 🎯 Funcionalidades

| Funcionalidade | Descrição |
|---|---|
| ➕ Adicionar | Nova tarefa via input ou tecla Enter |
| ✅ Marcar | Toggle concluída / pendente com clique |
| 🗑️ Remover | Remove uma tarefa específica |
| 🧹 Limpar | Remove todas as tarefas concluídas |
| 🔍 Filtrar | Ver todas / pendentes / concluídas |
| 📱 Responsivo | Funciona em PC e telemóvel |

---

## 📚 Conceitos demonstrados

### Backend (Flask)
| Conceito | Onde é aplicado |
|---|---|
| Rotas Flask | `@app.route()` com GET, POST, PATCH, DELETE |
| API REST | Endpoints JSON para cada operação |
| `jsonify()` | Serialização de respostas JSON |
| `request.get_json()` | Leitura do corpo do pedido |
| Validação | Verificação de dados antes de processar |
| Lista em memória | Sem base de dados — `tarefas = []` |

### Frontend (HTML/CSS/JS)
| Conceito | Onde é aplicado |
|---|---|
| `fetch()` API | Comunicação assíncrona com o backend |
| `async/await` | Chamadas assíncronas sem callbacks |
| DOM manipulation | Renderização dinâmica da lista |
| CSS Variables | Tema coerente e fácil de customizar |
| Responsive Design | `clamp()`, `flexbox`, media queries |
| Escape XSS | `escapeHtml()` antes de inserir no DOM |

---

## 🛠️ Como executar

### 1. Instalar dependências
```bash
pip install flask
```

### 2. Executar o servidor
```bash
python app.py
```

### 3. Abrir no browser
```
http://localhost:5000
```

### 4. Aceder pelo telemóvel (mesmo Wi-Fi)
```
http://<IP-do-teu-computador>:5000
```
> Para saber o teu IP: `ipconfig` (Windows) ou `ifconfig` (Mac/Linux)

---

## 📁 Estrutura do projeto

```
todo-list-flask/
├── app.py              ← backend Flask (API REST)
├── templates/
│   └── index.html      ← frontend (HTML + CSS + JS)
└── README.md
```

---

## 🔗 Versões relacionadas

| Versão | Repositório |
|---|---|
| Terminal em C | [todo-list-c](https://github.com/gabrielgrac/todo-list-c) |
| Terminal em Python | [todo-list-python](https://github.com/gabrielgrac/todo-list-python) |
| **Web com Flask** | este repositório |

---

## 💡 Possíveis extensões

- [ ] Persistência com SQLite ou ficheiro JSON
- [ ] Autenticação de utilizadores
- [ ] Deploy no Render / Railway (acesso público)
- [ ] Prioridades e datas de entrega
- [ ] Drag & drop para reordenar tarefas

---

## 📜 Licença

MIT — usa e modifica à vontade.
