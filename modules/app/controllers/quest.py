''' controller and routes for bills '''
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

        # except:
        #     return jsonify({'ok': False, 'message': 'Database unreachable'}), 500


    # if request.method == 'POST':
    #     data = request.get_json(force=True)
    #     if data.get('id', None) is not None and data.get('client_id', None) is not None and data.get('sum', None) is not None:
    #         mongo.db.Test.insert_one(data)
    #         return jsonify({'ok': True, 'message': 'Bills created successfully!'}), 200
    #     else:
    #         return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400
    #
    # if request.method == 'DELETE':
    #     if data.get('id', None) is not None:
    #         db_response = mongo.db.Test.delete_one({'id': data['id']})
    #         if db_response.deleted_count == 1:
    #             response = {'ok': True, 'message': 'record deleted'}
    #         else:
    #             response = {'ok': True, 'message': 'no record found'}
    #         return jsonify(response), 200
    #     else:
    #         return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400
    #
    # if request.method == 'PATCH':
    #     data = request.get_json(force=True)
    #     if data.get('query', {}) != {}:
    #         mongo.db.Test.update_one(
    #             data['query'], {'$set': data.get('payload', {})})
    #         return jsonify({'ok': True, 'message': 'record updated'}), 200
    #     else:
    #         return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400
