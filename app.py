from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {

    'id': 1,
    'titulo': 'teste',
    'autor': 'o testador'

    },
     {

    'id': 2,
    'titulo': 'teste 2',
    'autor': 'o testador 2'

    },
     {

    'id': 3,
    'titulo': 'teste 3',
    'autor': 'o testador 3'

    },
]

@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['GET'])
def obter_livros_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livros_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livro)

@app.route('/livros-create', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

@app.route('/livros/delete/<int:id>', methods=['DELETE'])
def  deleta_livro(id):
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
           del livros[indice]

    return jsonify(livros)






app.run(port=5000,host='localhost',debug=True)
