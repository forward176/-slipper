import sqlite3


START_ENERGY = 1_000


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



# assert is_user_exist(40) == False
# assert is_user_exist(200) == True
# x = 555
# update_clicks(200, x) 
# assert get_user_data(200) == (x, 5000, 0)
