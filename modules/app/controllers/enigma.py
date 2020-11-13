''' controller and routes for enigma '''
import os
from flask import request, jsonify, render_template
from app import app, mongo
import logger
import json

ROOT_PATH = os.environ.get('ROOT_PATH')
LOG = logger.get_root_logger(
    __name__, filename=os.path.join(ROOT_PATH, 'output.log'))

@app.route('/enigma/<id_quest>/<id_enigma>', methods=['GET'])
def enigma(id_quest, id_enigma):
    if request.method == 'GET':
        query = request.args
        try:
            data = mongo.db.enigma.find_one({"id_quest": int(id_quest), "id_enigma": int(id_enigma)})
            return render_template("enigma.html", data=data), 200
        except Exception as e:
             return jsonify({'ok': False, 'message': str(e)}), 500
