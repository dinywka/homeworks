#1
# import requests
# import json
#
# url = "https://jsonplaceholder.typicode.com/todos"
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/102.0.0.0 Safari/537.36'
# }
# data = requests.get(url=url, headers=headers).json()
#
# class Post:
#     def __init__(self, user_id: int, id: int, title: str, completed: str):
#         self.user_id = user_id
#         self.id = id
#         self.title = title
#         self.completed = completed
#
#     def create_dict(self):
#         return {
#             "user_id": self.user_id,
#             "id": self.id,
#             "title": self.title,
#             "completed": self.completed
#         }
#
# post_list = []
# for post_data in data:
#     post = Post(post_data['userId'], post_data['id'], post_data['title'], post_data['completed'])
#     post_dict = post.create_dict()
#     post_list.append(post_dict)
#
# with open("new_json.json", "w") as file:
#     json.dump(post_list, file)

#10
import psycopg2
from psycopg2.extras import execute_values
def change_table():
    conn = psycopg2.connect(
            user="postgres",
            password="28031989",
            host="127.0.0.1",
            port="5432",
            database="hw10.03.23"
    )

    cur = conn.cursor()

    cur.execute("SELECT id, title FROM hw")
    rows = cur.fetchall()

    for row in rows:
        id = row[0]
        title = row[1]
        new_title = f"{title}_{id}"
        update_sql = f"UPDATE hw SET title = '{new_title}' WHERE id = {id}"
        cur.execute(update_sql)


    cur.execute("DELETE FROM hw WHERE title ~* '.*[13579].*'")
    conn.commit()
change_table()

#11
#1
# n=int(input())
# s=0
# for i in range(1, n+1):
#     s+=i
# for i in range(n-1):
#     s-=int(input())
# print(s)

#2
# n=int(input())
# for i in range(1, n+1):
#     if i**2<=n:
#         print(i**2, end=" ")

