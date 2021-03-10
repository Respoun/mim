''' controller and routes for enigma '''
import os
from datetime import timedelta, date, datetime
from flask import jsonify, request, make_response, send_from_directory, render_template, session
from app import app, mongo
import logger
import json
import sys

ROOT_PATH = os.environ.get('ROOT_PATH')
LOG = logger.get_root_logger(
    __name__, filename=os.path.join(ROOT_PATH, 'output.log'))

@app.route('/enigma/<id_quest>/<id_enigma>', methods=['GET'])
def enigma(id_quest, id_enigma):
    if request.method == 'GET':

        #GESTION CHRONO
        if session.get('time_start') is None:
            now = datetime.now()
            dt_string = now.strftime("%Y:%m:%d:%I:%M:%S")
            session['time_start'] = dt_string
        now = datetime.now()
        s2 = now.strftime("%Y:%m:%d:%I:%M:%S")
        s1 = session['time_start']
        d1 = datetime.strptime(s1,'%Y:%m:%d:%I:%M:%S')
        d2 = datetime.strptime(s2,'%Y:%m:%d:%I:%M:%S')
        chrono = str(int((d2-d1).total_seconds()/60))

        query = request.args
        try:
            data = mongo.db.enigma.find_one({"id_quest":id_quest, "id_enigma":id_enigma})
            if int(data["id_img"]) != 0:
                img = mongo.db.Img.find_one({"id": int(data["id_img"])})
                return render_template("enigma.html", data=data, chrono=chrono, img=img), 200
            else:
                return render_template("enigma.html", data=data, chrono=chrono), 200
        except Exception as e:
             return jsonify({'ok': False, 'message': str(e)}), 500
