#1
import psycopg2
from psycopg2.extras import execute_values
def insert_to_table(my_data):

    with psycopg2.connect(
            user="postgres",
            password="28031989",
            host="127.0.0.1",
            port="5432",
            database="hw10.03.23"
    ) as connection:
        with connection.cursor() as cursor:
            insert_data = """INSERT INTO hw (id, title, description, success, deadline, data_created) VALUES %s"""
            execute_values(cursor, insert_data, my_data)
            # cursor.execute("""INSERT INTO hw (id, title, description, success, deadline, data_created) VALUES ('1', 'Title1',
            # 'Description1', true, '27.01.2022', '26.01.2022')""")

my_data = [('1', 'Title1', 'Description1', 'true', '2022-01-27', '2022-01-26'),
           ('2', 'Title2', 'Description2', 'false', '2022-06-27', '2022-06-25'),
           ('3', 'Title3', 'Description3', 'true', '2022-01-27', '2022-01-23'),
           ('4', 'Title4', 'Description4', 'false', '2022-01-27', '2022-01-27'),
           ('5', 'Title5', 'Description5', 'true', '2022-01-27', '2022-01-25')]

if __name__ == "__main__":
    insert_to_table(my_data)




# #6
# s = int(input("Введите стоимость подписки на оелайн-кинотеатр:"))
# p = int(input("Введите стоимость пиццы:"))
# m = int(input("Введите размер зарплаты:"))
# if s+p<=m:
#     print("Да")
# else:
#     print("Нет")
#
# #7
# figure = input("Выберите фигуру: ладья, король, конь или ферзь ")
# a, a1, b, b1 = input().split()
# try:
#     if figure == "ладья":
#         a=int(a)
#         a1=int(a1)
#         b=int(b)
#         b1=int(b1)
#         if b==a or b1==a1:
#             print("YES")
#         else:
#             print("NO")
#     elif figure == "король":
#         a=int(a)
#         a1=int(a1)
#         b=int(b)
#         b1=int(b1)
#         if abs(a-b)<=1 and abs(a1-b1)<=1:
#             print("YES")
#         else:
#             print("NO")
#     elif figure == "ферзь":
#         a=int(a)
#         a1=int(a1)
#         b=int(b)
#         b1=int(b1)
#         if abs(a-b) == abs(a1-b1) or a==b or a1==b1:
#             print("YES")
#         else:
#             print("NO")
#     elif figure == "конь":
#         a=int(a)
#         a1=int(a1)
#         b=int(b)
#         b1=int(b1)
#         if (abs(b-a)-a) == 2 and abs(a1-b1==1) or (abs(b-a) == 1 and abs(a1-b1)==2):
#             print("YES")
#         else:
#             print("NO")
#     else:
#         print("Введите корректную фигуру")
# except ValueError:
#     print("Error. Value Error")
# except:
#     print("Something else went wrong")