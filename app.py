"""
============================================================
 TODO LIST — Versão Web com Flask
 Autor  : <seu nome>
 Versão : 2.0.0
 Licença: MIT

 Conceitos demonstrados:
   - Flask (rotas, métodos GET/POST/DELETE/PATCH)
   - API REST simples com JSON
   - Lista em memória (sem base de dados)
   - Separação backend / frontend
   - Responsivo — funciona em PC e telemóvel

 Instalar dependências:
   pip install flask

 Executar:
   python app.py

 Abrir no browser:
   http://localhost:5000
============================================================
"""

from flask import Flask, jsonify, request, render_template
from datetime import datetime

app = Flask(__name__)

# ── Estrutura de dados em memória ─────────────────────────
# Cada tarefa é um dicionário com:
#   id        : identificador único
#   descricao : texto da tarefa
#   concluida : bool
#   criada_em : data/hora de criação
tarefas = []
proximo_id = 1   # contador de IDs


# ══════════════════════════════════════════════════════════
#  ROTAS HTML
# ══════════════════════════════════════════════════════════

@app.route("/")
def index():
    """Serve a página principal."""
    return render_template("index.html")


# ══════════════════════════════════════════════════════════
#  API REST — endpoints JSON
# ══════════════════════════════════════════════════════════

@app.route("/api/tarefas", methods=["GET"])
def listar_tarefas():
    """
    GET /api/tarefas
    Devolve todas as tarefas em formato JSON.
    """
    return jsonify(tarefas)


@app.route("/api/tarefas", methods=["POST"])
def adicionar_tarefa():
    """
    POST /api/tarefas
    Body JSON: {"descricao": "texto da tarefa"}
    Cria uma nova tarefa e devolve-a.
    """
    global proximo_id

    dados = request.get_json()

    # validação: descrição obrigatória e não vazia
    if not dados or not dados.get("descricao", "").strip():
        return jsonify({"erro": "Descrição não pode ser vazia"}), 400

    tarefa = {
        "id"       : proximo_id,
        "descricao": dados["descricao"].strip(),
        "concluida": False,
        "criada_em": datetime.now().strftime("%d/%m/%Y %H:%M")
    }

    tarefas.append(tarefa)
    proximo_id += 1

    return jsonify(tarefa), 201


@app.route("/api/tarefas/<int:tarefa_id>", methods=["PATCH"])
def marcar_concluida(tarefa_id):
    """
    PATCH /api/tarefas/<id>
    Alterna o estado concluída/pendente de uma tarefa.
    """
    tarefa = next((t for t in tarefas if t["id"] == tarefa_id), None)

    if tarefa is None:
        return jsonify({"erro": "Tarefa não encontrada"}), 404

    tarefa["concluida"] = not tarefa["concluida"]   # toggle
    return jsonify(tarefa)


@app.route("/api/tarefas/<int:tarefa_id>", methods=["DELETE"])
def remover_tarefa(tarefa_id):
    """
    DELETE /api/tarefas/<id>
    Remove uma tarefa pelo id.
    """
    global tarefas

    tarefa = next((t for t in tarefas if t["id"] == tarefa_id), None)

    if tarefa is None:
        return jsonify({"erro": "Tarefa não encontrada"}), 404

    tarefas = [t for t in tarefas if t["id"] != tarefa_id]
    return jsonify({"mensagem": "Tarefa removida com sucesso"})


@app.route("/api/tarefas/concluidas", methods=["DELETE"])
def remover_concluidas():
    """
    DELETE /api/tarefas/concluidas
    Remove todas as tarefas marcadas como concluídas.
    """
    global tarefas

    antes = len(tarefas)
    tarefas = [t for t in tarefas if not t["concluida"]]
    removidas = antes - len(tarefas)

    return jsonify({"removidas": removidas})


# ══════════════════════════════════════════════════════════
#  PONTO DE ENTRADA
# ══════════════════════════════════════════════════════════

if __name__ == "__main__":
    # debug=True: recarrega automaticamente ao guardar o ficheiro
    # host="0.0.0.0": acessível na rede local (telemóvel no mesmo Wi-Fi)
    app.run(debug=True, host="0.0.0.0", port=5000)
