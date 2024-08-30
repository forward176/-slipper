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
            click_count = 0
            if 'refresh_page' in data:
                print('обновление страницы!')
                tg_id = data['value']
                file_path = f'user_data/{tg_id}.txt'
                if os.path.exists(file_path):

                    with open(file_path, 'r', encoding='UTF-8') as file:
                        click_count = file.read()
                        print(click_count)
                else:
                    with open(file_path, 'w', encoding='UTF-8') as file:
                        file.write('0')
                        print('Файл создан')
                    
                return jsonify({'message': 'Success!', 'value': click_count}), 200
            elif 'new_click_count' in data:
                tg_id = data['value']
                new_click_count = data['new_click_count']
                file_path = f'user_data/{tg_id}.txt'
                with open(file_path, 'w', encoding='UTF-8') as file:
                    file.write(f'{new_click_count}')                   
                return jsonify({'message': 'Success!'}), 200

            else:
                raise KeyError('Value key not found')
        except (KeyError, json.JSONDecodeError) as e:
            print('&&&&')
            return jsonify({'error': 'Invalid data format'}), 400
        
