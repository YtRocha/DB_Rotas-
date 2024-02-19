from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = {}

@app.route('/usuario', methods=['POST'])
def criar_usuario():
    dados_usuario = request.json
    cpf = dados_usuario.get('cpf')
    if cpf in usuarios:
        return jsonify({'mensagem': 'Usuário já existe'}), 400
    usuarios[cpf] = {
        'cpf': cpf,
        'nome': dados_usuario.get('nome'),
        'data_nascimento': dados_usuario.get('data_nascimento')
    }
    return jsonify({'mensagem': 'Usuário criado com sucesso'},{'usuario':usuarios[cpf]}), 201

@app.route('/usuario/<cpf>', methods=['GET'])
def obter_usuario(cpf):
    if cpf in usuarios:
        return jsonify(usuarios[cpf])
    else:
        return jsonify({'mensagem': 'Usuário não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
