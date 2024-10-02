from flask import Flask, render_template, request, jsonify
import json
import sqlite3
import DB
from datetime import datetime


connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

app = Flask(__name__)
 

def restore(energy, last_online):
    delta_time = int((datetime.now() - last_online).total_seconds())
    energy += delta_time
    if energy > DB.MAX_ENERGY:
        energy = DB.MAX_ENERGY
    return energy


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        try:
            data = request.json
            if 'refresh_page' in data:
                tg_id = data['tg_id']
                if not DB.is_user_exist(tg_id):
                    DB.create_user(tg_id)
                click_count, energy, last_online = DB.get_user_data(tg_id)
                energy = restore(energy, last_online)
                return jsonify({'click_count': click_count, 'energy': energy}), 200
            elif 'new_click_count' in data:
                tg_id = data['tg_id']
                new_click_count = data['new_click_count']
                energy = data['energy']
                # DB.update_clicks(tg_id, new_click_count)  
                DB.update_user_data(tg_id, new_click_count, energy)                             
                return jsonify({'message': 'Success!'}), 200
            else:
                raise KeyError('Value key not found')
        except (KeyError, json.JSONDecodeError) as e:
            print('&&&&')
            return jsonify({'error': 'Invalid data format'}), 400
