#Поднять сервер с возвратом данных
#Получить данные из формы и вывести json в консоль
#Создать бд и функцию, кот записывает рац предложение

from fastapi import FastAPI, Request
from typing import Annotated
from fastapi import FastAPI, Form
import sqlite3


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

def sqlite_create_posts_db():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
CREATE TABLE IF NOT EXISTS ideas
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT
)
''')

@app.post("/insert")
async def post_list_post(request: Request):
    form = await request.form()
    title = form.get('title')
    print(title)
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
    INSERT INTO ideas
    (title) VALUES (?)
    ''', (title,))
    return {"message": "title"}

def check():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
    SELECT * FROM ideas
    ''')
        data = cursor.fetchall()
        print(data)

check()





