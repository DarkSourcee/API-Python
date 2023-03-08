from flask import Blueprint, jsonify, request
from Model.fornecedore import Fornecedores
from config.response import response
import jwt

fornecedores = Blueprint('fornecedores', __name__)

# Rota para listar todos os registros na tabela "usuarios"
@fornecedores.route('/fornec', methods=['GET'])
def listar_fornecedores():
    try:
        fornecedores = Fornecedores.listaFornecedor()
        return response(error="", data=fornecedores, status=200)
    except:
        return response(error="Erro na consulta", data="", status=401)

# Rota para buscar um usuário pelo ID
@fornecedores.route('/fornec/<int:id>', methods=['GET'])
def buscar_fornec(id):
    try:
        fornecedores = Fornecedores.listaFornecedoresPorID(id)
        return jsonify(fornecedores)
    except:
        return response(error="Erro na consulta", data="", status=401)

# # Rota para cadastrar um novo usuário
@fornecedores.route('/fornec', methods=['POST'])
def cadastrar_fornec():
    try:
        token = request.headers.get('Authorization')
        decoded_token = jwt.decode(token, 'minha_chave_secreta', algorithms=['HS256'])
        usuario_id = decoded_token['user_id']
        dados = {
            "nome" : request.json['nome'],
            "email" : request.json['email'],
            "telefone" : request.json['telefone'],
            "id" : usuario_id
        }
        Fornecedores.cadastraFornecedor(dados)
        return response(error="", data="Usuário cadastrado com sucesso!", status=200)    
    except KeyError:
        return response(error="Erro na inserção dados", data="", status=401)
    except Exception as e:
        return response(error=f"Erro ao autenticar usuário: {str(e)}", data="", status=401)

# # Rota para atualizar os dados de um usuário pelo ID
@fornecedores.route('/fornec/<int:id>', methods=['PUT'])
def atualizar_fornec(id):
    try:
        dados = {
            "id" : id,
            "nome" : request.json['nome'],
            "email" : request.json['email'],
            "telefone" : request.json['telefone']
        }
        Fornecedores.atualizarFornecedor(dados)
        return response(error="", data="Fornecedor atualizado com sucesso!", status=200)
    except:
        return response(error="Erro na consulta", data="", status=401)

# # Rota para excluir um usuário pelo ID
@fornecedores.route('/fornec/<int:id>', methods=['DELETE'])
def excluir_fornec(id):
    try:
        Fornecedores.deletarFornecedor(id)
        return response(error="", data="Fornecedor excluído com sucesso!", status=200)
    except:
        return response(error="Erro na consulta", data="", status=401)

