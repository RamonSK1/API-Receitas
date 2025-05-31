from flask import Blueprint, jsonify, request
from .model import Receita, IngredienteQuantidade, Ingrediente
from . import db

bp = Blueprint('main', __name__)

@bp.route('/receitas', methods=['GET'])
def get_receitas():
    receitas = Receita.query.all()
    result = []
    for r in receitas:
        ingredientes_list = [{
            'id': iq.id,
            'ingrediente_id': iq.ingrediente_id,
            'quantidade': iq.quantidade
        } for iq in r.ingredientes]

        receita_dict = {
            'id': r.id,
            'nome': r.nome,
            'ingredientes': ingredientes_list,
            'modo_preparo': r.modo_preparo
        }
        result.append(receita_dict)

    return jsonify(result)
