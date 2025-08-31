from flask import Flask, jsonify, request #aqui eu importei o flask que será nosso server, o jsonify que transforma dicionarios em json e o request que pega os dados que estão trafegando na requisição

app = Flask(__name__) #aqui eu criei o server/aplicação flask com o nome do arquivo

#base de dados (lista de dicionários)
livros = [
    {
        'id': 1,
        'titulo':'O senhor dos anéis - A sociedade do anel',
        'autor': 'J.R.R. Tolkien'
    },
    {
        'id': 2,
        'titulo':'Harry Potter e a pedra filosofal',
        'autor': 'J.K. Rowling'
    },
    {
        'id': 3,
        'titulo':'Interestelar - A origem do universo',
        'autor': 'Christopher Nolan'
    },
]

#Consultar (todos)
#deve-se criar uma função para cada endpoint
@app.route('/livros', methods=['GET']) #aqui eu criei o endpoint /livros que aceita apenas o método GET
def obter_livros():
    return jsonify(livros) #aqui eu retorno a lista de livros em formato json

#Consultar (por id)
@app.route('/livros/<int:id>', methods=['GET']) #aqui eu criei o endpoint /livros/<id> que aceita apenas o método GET e recebe um parâmetro id do tipo inteiro
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

#Editar
@app.route('/livros/<int:id>', methods=['PUT']) #aqui eu criei o endpoint /livros/<id> que aceita apenas o método PUT e recebe um parâmetro id do tipo inteiro
def editar_livro_por_id(id):
    livro_alterado = request.get_json() #aqui eu pego o json que veio na requisição, os dados que o cliente enviou
    for indice,livro in enumerate(livros): #aqui eu uso o enumerate para pegar o índice e o livro ao mesmo tempo
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
        
#Criar
@app.route('/livros',methods=['POST']) #aqui eu criei o endpoint /livros que aceita apenas o método POST
def incluir_novo_livro():
    novo_livro = request.get_json() #aqui eu pego o json que veio na requisição, os dados que o cliente enviou e guardo na variável novo_livro
    livros.append(novo_livro) #aqui eu adiciono o novo livro na lista de livros
    return jsonify(livros) #aqui eu retorno a lista de livros em formato json
#Excluir
@app.route('/livros/<int:id>', methods=['DELETE']) #aqui eu criei o endpoint /livros/<id> que aceita apenas o método DELETE e recebe um parâmetro id do tipo inteiro
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id')==id:
            del livros[indice]
            return jsonify(livros) 
app.run(port=5000, host='localhost', debug=True) #aqui eu rodo o server na porta 5000 do localhost e com o debug ativo para atualizar automaticamente quando eu salvar o arquivo