import sqlite3
from datetime import datetime

START_ENERGY = 2_000
MAX_ENERGY = 2_000

def is_user_exist(telegram_id: int) -> bool:
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    query = '''
        SELECT * 
        FROM Users
        WHERE tg_id=?;
    '''
    cursor.execute(query, (telegram_id, ))    
    users = cursor.fetchall()
    connection.close()
    return bool(users)


def get_user_data(telegram_id: int) -> tuple:
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    query = '''
        SELECT clicks, energy, last_online
        FROM Users
        WHERE tg_id=?;
    '''
    cursor.execute(query, (telegram_id, ))    
    users = cursor.fetchall()   
    connection.close()
    return users[0]

def create_user(telegram_id: int) -> None:
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    query = '''
        INSERT INTO Users
        VALUES (?, 0, ?, 0);
    '''
    cursor.execute(query, (telegram_id, START_ENERGY))    
    connection.commit()
    connection.close()

# сейчас не используется
def update_clicks(tg_id:int, new_click_count:int) -> None: 
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    query = '''
            UPDATE Users  
            SET clicks = ?
            WHERE tg_id = ?;
    '''
    cursor.execute(query, (new_click_count, tg_id))    
    connection.commit()
    connection.close()

def update_user_data(tg_id:int, new_click_count: int, energy: int) -> None: 
    current_datetime = datetime.now()
    print(current_datetime)
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    query = '''
            UPDATE Users  
            SET clicks = ?, energy = ?, last_online = ?
            WHERE tg_id = ?;
    '''
    data_tuple = (new_click_count, energy, current_datetime, tg_id)
    cursor.execute(query, data_tuple)    
    connection.commit()
    connection.close()

# create_user(100)
# update_user_data(100, 200, 400)
# assert is_user_exist(40) == False
# assert is_user_exist(200) == True
# x = 555
# update_clicks(200, x) 
# assert get_user_data(200) == (x, 5000, 0)
