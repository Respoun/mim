''' controller and routes for quest '''
import os
from flask import request, jsonify, render_template
from app import app, mongo
import logger
import json

ROOT_PATH = os.environ.get('ROOT_PATH')
LOG = logger.get_root_logger(
    __name__, filename=os.path.join(ROOT_PATH, 'output.log'))


@app.route('/quest', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def test():
    if request.method == 'GET':
        query = request.args
        try:
            data = mongo.db.quest.find()
            response = []
            for document in data:
                document['_id'] = str(document['_id'])
                response.append(document)
            return render_template("quest.html", response=response), 200
        except Exception as e:
             return jsonify({'ok': False, 'message': str(e)}), 500
