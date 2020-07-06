import uuid
import psycopg2
conn = psycopg2.connect(dbname='yd', user='postgres', 
                        password='Homyak17', host='82.146.38.230',
                        port='5432'
                        )
cursor = conn.cursor()

# запросы для создания таблиц в db.sqlite
query_tasks = """CREATE TABLE IF NOT EXISTS tasks (
                    id SERIAL PRIMARY KEY, 
                    task TEXT,
                    uuid TEXT,
                    done TEXT)"""
# выполнение запросов на создание таблиц
cursor.execute(query_tasks)
u1 = uuid.uuid4()
print(u1)
u2 = uuid.uuid4()
print(u2)
u3 = uuid.uuid4()
print(u3)
u4 = uuid.uuid4()
print(u4)
query_task= """INSERT INTO tasks (task, uuid, done) VALUES ('{0}', '{1}', '{2}')""".format("Илья", u1, "-")
cursor.execute(query_task)
query_task= """INSERT INTO tasks (task, uuid, done) VALUES ('{0}', '{1}', '{2}')""".format("Леха", u2, "-")
cursor.execute(query_task)
query_task= """INSERT INTO tasks (task, uuid, done) VALUES ('{0}', '{1}', '{2}')""".format("Ваня", u3, "-")
cursor.execute(query_task)
query_task= """INSERT INTO tasks (task, uuid, done) VALUES ('{0}', '{1}', '{2}')""".format("Дима", u4, "-")
cursor.execute(query_task)
query_task= """DELETE FROM tasks WHERE task = ('{0}')""".format("Помыть посуду")
cursor.execute(query_task)
# query_print = """SELECT * FROM tasks"""
# cursor.execute(query_print)
# print(cursor.fetchall())

# закрываем соединение к БД
conn.commit()
cursor.close()
conn.close()
print("База данных успешно создана!")

