import uuid
import psycopg2

# подключение к БД
def connect_db():
    conn = psycopg2.connect(dbname='yd', user='postgres', 
                        password='password', host='host',
                        port='5432'
                        )
    return conn

# закрываем подключение к БД
def close_db(conn):
    conn.commit()

# выбор всех записей из БД
def select_in_table():
    conn = connect_db()
    cursor = conn.cursor()
    query_select = """SELECT * FROM tasks ORDER BY id ASC"""
    cursor.execute(query_select)
    result = cursor.fetchall()
    close_db(conn)
    
    return result

# добавление записи в БД
def insert_in_table(task):
    conn = connect_db()
    cursor = conn.cursor()
    uuid_insert = uuid.uuid4()
    query_task= """INSERT INTO tasks (task, uuid, done) VALUES ('{0}', '{1}', '{2}')""".format(task, uuid_insert, "-")
    cursor.execute(query_task)
    close_db(conn)

# удаление записи в БД
def delete_from_table(uuid):
    conn = connect_db()
    cursor = conn.cursor()
    query_delete = """DELETE FROM tasks WHERE uuid = ('{0}')""".format(uuid)
    cursor.execute(query_delete)
    close_db(conn)

# просмотр выполнения
def check_done(uuid):
    conn = connect_db()
    cursor = conn.cursor()
    query_select = """SELECT done FROM tasks WHERE uuid = {0}""".format(uuid)
    cursor.execute(query_select)
    result = cursor.fetchall()
    close_db(conn)
    
    return result

# ставим решение
def set_done(uuid):
    conn = connect_db()
    cursor = conn.cursor()
    state = "+"
    query_update= """UPDATE tasks SET done = '{0}' WHERE uuid = '{1}'""".format(state, uuid)
    cursor.execute(query_update)
    close_db(conn)    