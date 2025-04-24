from flask import Flask, jsonify, request
from flask_migrate import Migrate
from model import db, Ingrediente, Receita, IngredienteQuantidade
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/ingredientes', methods=['GET', 'POST'])
def manage_ingredientes():
    if request.method == 'GET':
        ingredientes = Ingrediente.query.all()
        return jsonify([{'id': i.id, 'nome': i.nome, 'unidade_medida': i.unidade_medida} for i in ingredientes])
    
    if request.method == 'POST':
        data = request.json
        novo_ingrediente = Ingrediente(nome=data['nome'], unidade_medida=data['unidade_medida'])
        db.session.add(novo_ingrediente)
        db.session.commit()
        return jsonify({'id': novo_ingrediente.id}), 201

@app.route('/ingredientes/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def ingrediente_detail(id):
    ingrediente = Ingrediente.query.get_or_404(id)
    
    if request.method == 'GET':
        return jsonify({'id': ingrediente.id, 'nome': ingrediente.nome, 'unidade_medida': ingrediente.unidade_medida})
    
    if request.method == 'PUT':
        data = request.json
        ingrediente.nome = data['nome']
        ingrediente.unidade_medida = data['unidade_medida']
        db.session.commit()
        return jsonify({'id': ingrediente.id})
    
    if request.method == 'DELETE':
        db.session.delete(ingrediente)
        db.session.commit()
        return '', 204

@app.route('/receitas', methods=['GET', 'POST'])
def manage_receitas():
    if request.method == 'GET':
        receitas = Receita.query.all()
        return jsonify([{'id': r.id, 'nome': r.nome, 'modo_preparo': r.modo_preparo} for r in receitas])
    
    if request.method == 'POST':
        data = request.json
        nova_receita = Receita(nome=data['nome'], modo_preparo=data['modo_preparo'])
        db.session.add(nova_receita)
        db.session.commit()
        return jsonify({'id': nova_receita.id}), 201

@app.route('/receitas/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def receita_detail(id):
    receita = Receita.query.get_or_404(id)
    
    if request.method == 'GET':
        ingredientes_quantidade = IngredienteQuantidade.query.filter_by(receita_id=id).all()
        ingredientes = [{'ingrediente_id': iq.ingrediente_id, 'quantidade': iq.quantidade} for iq in ingredientes_quantidade]
        return jsonify({
            'id': receita.id,
            'nome': receita.nome,
            'modo_preparo': receita.modo_preparo,
            'ingredientes': ingredientes
        })
    
    if request.method == 'PUT':
        data = request.json
        receita.nome = data['nome']
        receita.modo_preparo = data['modo_preparo']
        db.session.commit()
        return jsonify({'id': receita.id})
    
    if request.method == 'DELETE':
        db.session.delete(receita)
        db.session.commit()
        return '', 204

@app.route('/receitas/<int:receita_id>/ingredientes', methods=['POST'])
def adicionar_ingrediente_na_receita(receita_id):
    receita = Receita.query.get_or_404(receita_id)
    data = request.json

    ingrediente = Ingrediente.query.get_or_404(data['ingrediente_id'])

    nova_relacao = IngredienteQuantidade(
        ingrediente_id=ingrediente.id,
        receita_id=receita.id,
        quantidade=data['quantidade']
    )

    db.session.add(nova_relacao)
    db.session.commit()

    return jsonify({
        'receita_id': receita.id,
        'ingrediente_id': ingrediente.id,
        'quantidade': data['quantidade']
    }), 201

if __name__ == '__main__':
    app.run(debug=True)
