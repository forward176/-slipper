from flask import Flask, render_template, request, jsonify
import json
import os.path

app = Flask(__name__)
 
 
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        print('!!!!')
        return render_template('index.html')
    elif request.method == 'POST':
        print('@@@@')
        try:
            data = request.json
            test = 'нет данных'
            if 'value' in data:
            
                tg_id = data['value']
                file_path = f'user_data/{tg_id}.txt'
                if os.path.exists(file_path):

                    with open(file_path, 'r', encoding='UTF-8') as file:
                        test = file.read()
                        print(test)
                else:
                    with open(file_path, 'w', encoding='UTF-8') as file:
                        file.write('0')
                        print('Файл создан')
                    
                return jsonify({'message': 'Success!', 'value': test}), 200
            else:
                raise KeyError('Value key not found')
        except (KeyError, json.JSONDecodeError) as e:
            print('&&&&')
            return jsonify({'error': 'Invalid data format'}), 400
        
