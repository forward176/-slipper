import sqlite3


connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# CRUD -- CREATE - READ - UPDATE - DELETE


# - удаление
# cursor.execute('''
#     DROP TABLE Users; 
# ''')
# connection.commit()

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Users (
#         tg_id INTEGER PRIMARY KEY,
#         clicks INTEGER,
#         energy INTEGER,
#         last_online TIMESTAMP
#     );
# ''')




# cursor.execute('''
#     INSERT INTO Users - добавить данные в таблицу 
#     VALUES (200, 500, 2000, 0);
# ''')

# cursor.execute('''
#     UPDATE Users 
#     SET energy=10000
#     WHERE tg_id=100;
# ''')

# cursor.execute('''
#     UPDATE Users 
#     SET energy=5000;
# ''')

# cursor.execute('''
#     DELETE FROM Users 
#     WHERE tg_id=100;
# ''')

# cursor.execute('''
#     SELECT tg_id, energy - выбрать\ получить данные
#     FROM Users;
# ''')
# users = cursor.fetchall()
# print(users)

# cursor.execute('''
#     SELECT * 
#     FROM Users
#     WHERE tg_id=200;
# ''')
# users = cursor.fetchall()
# print(users)

connection.commit()
connection.close()