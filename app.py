from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista inicial de estudantes
estudantes = [
    {
        'matricula': 1,
        'nome': 'Alberto',
        'materia': 'Português',
        'nota': 10,
    },
    {
        'matricula': 2,
        'nome': 'Bruno',
        'materia': 'Inglês',
        'nota': 9,
    },
    {
        'matricula': 3,
        'nome': 'Carlos',
        'materia': 'Português',
        'nota': 4,
    },
    {
        'matricula': 4,
        'nome': 'Diogo',
        'materia': 'Inglês',
        'nota': 7,
    },
]

# Consultar todos os estudantes
@app.route('/estudantes', methods=['GET'])
def obter_estudantes():
    return jsonify(estudantes)

# Consultar estudante por matrícula
@app.route('/estudantes/<int:matricula>', methods=['GET'])
def obter_estudante_por_matricula(matricula):
    for estudante in estudantes:
        if estudante.get('matricula') == matricula:
            return jsonify(estudante)
    return jsonify({"erro": "Estudante não encontrado"}), 404

# Criar novo estudante
@app.route('/estudantes', methods=['POST'])
def incluir_novo_estudante():
    novo_estudante = request.get_json()
    estudantes.append(novo_estudante)
    return jsonify(novo_estudante), 201

# Editar estudante existente
@app.route('/estudantes/<int:matricula>', methods=['PUT'])
def editar_estudante(matricula):
    estudante_alterado = request.get_json()
    for indice, estudante in enumerate(estudantes):
        if estudante.get('matricula') == matricula:
            estudantes[indice].update(estudante_alterado)
            return jsonify(estudantes[indice])
    return jsonify({"erro": "Estudante não encontrado"}), 404

# Excluir estudante
@app.route('/estudantes/<int:matricula>', methods=['DELETE'])
def excluir_estudante(matricula):
    for indice, estudante in enumerate(estudantes):
        if estudante.get('matricula') == matricula:
            del estudantes[indice]
            return jsonify({"mensagem": "Estudante excluído com sucesso"}), 200
    return jsonify({"erro": "Estudante não encontrado"}), 404

# Executar a aplicação
if __name__ == '__main__':
    app.run(port=4040, host='localhost', debug=True)