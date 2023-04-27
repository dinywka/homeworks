import sys

import requests
import json
import os
from openpyxl import Workbook
import time

# Задание 1.
# [1 балл]
# 1) Выведите в консоль 5 звёздочек, используя умножение строк.
# 2) Напишите программу на Python, чтобы создать треугольник из звезд.

# print("*" * 5)
#
# def star_triangle(r):
#     for i in range(r):
#         print(" " * (r - i - 1) + "*" * (2 * i + 1))
#
# star_triangle(7)

# Задание 2.
# [2 балла]
# 1) Получите через http – запрос все объекты из jsonplaceholder todo.
# 2) Запишите все полученные данные в новую папку temp, в разные .json файлы.
# 3) Прочитайте все файлы из папки, и запишите данные каждого в единый .xlsx файл.


# response = requests.get("https://jsonplaceholder.typicode.com/todos")
#
# if not os.path.exists('temp'):
#         os.makedirs('temp')
#
# todos = response.json()
# for todo in todos:
#     filename = f'temp/{todo["id"]}.json'
#     with open(filename, 'w') as file:
#         json.dump(todo, file)
#
# all_todos = []
# for filename in os.listdir('temp'):
#     with open(f'temp/{filename}') as file:
#         todo = json.load(file)
#         all_todos.append(todo)
#
# wb = Workbook()
# ws = wb.active
#
# headers = ['userId', 'id', 'title', 'completed']
# ws.append(headers)
#
# for todo in all_todos:
#     row = [todo['userId'], todo['id'], todo['title'], todo['completed']]
#     ws.append(row)
#
# wb.save('all_todos.xlsx')


# Задание 3.
# [2 балла]
# 1) Напишите любой пример бесконечного таймера, через цикл while.
# 2) Модифицируйте код, чтобы можно было задать множитель для секунд от ввода пользователя.

# second = 0
# minute = 0
# hour = 0
# time_sleed = int(input("Введите множитель для секунд"))
# while True:
#     time.sleep(1)
#     second += time_sleed
#
#     if second>=59:
#         minute += 1
#         second = 0
#         if minute>=59:
#             hour += 1
#             minute = 0
#             if hour>=24:
#                 second = 0
#                 minite = 0
#                 hour = 0
#     print("{:02}:{:02}:{:02}".format(hour, minute, second))


# Задание 4.
# [3 балла]
# 1) Определите класс car с двумя атрибутами: color и speed. Затем создайте экземпляр и верните speed.
# 2) Модифицируйте код так, чтобы при старте программы, пользователь мог сам задать скорость машины, проверку выполните через регулярное выражение.

# import re
# class Car:
#     def __init__(self, color, speed):
#         self.color = color
#         self.speed = speed
#
#     def get_speed(self):
#         return self.speed
#
# color = input("Ввелите цвет машины: ")
# speed = input("Ввелите скорость машины: ")
#
# while not re.match(r'^\d+$', speed):
#     print("Скорость должна быть числом")
#     speed = input("Ввелите скорость машины: ")
#
# my_car = Car(color, int(speed))
# print(my_car.get_speed())

# 1) Реализуйте программу с интерфейсом на библиотеке pyqt5, необходимо чтобы при нажатии происходил запрос по адресу, введённому в textedit, статус запроса выводите в консоль.
# 2) Модифицируйте код так, чтобы статус запроса с описанием выводился в текстовое поле в инстерфейсе. Соберите программу в исполняемый файл, т.е. .exe .

import requests
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


# class MainWindow(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("My program")
#         self.resize(400, 300)
#
#         self.url_label = QLabel('URL адрес:')
#         self.url_edit = QLineEdit()
#         self.url_edit.setText('https://www.google.com')
#         self.status_label = QLabel('Статус запроса:')
#
#         self.button = QPushButton('Отправить запрос')
#         self.button.clicked.connect(self.send_request)
#
#         vbox = QVBoxLayout()
#         vbox.addWidget(self.url_label)
#         vbox.addWidget(self.url_edit)
#         vbox.addWidget(self.status_label)
#         vbox.addWidget(self.button)
#
#         self.setLayout(vbox)
#
#     def send_request(self):
#         url = self.url_edit.text()
#         response = requests.get(url)
#         status_code = response.status_code
#         print(f"Статус запроса: {status_code}")
#         self.status_label.setText(f"Статус запроса: {status_code}")
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())


# 1) Подбор пароля для тестирования: записать в документ в один поток числа от 1 до 100000.
# 2) Переписать логику на 10 мультипроцессов и в конце склейку в один.

import threading

class NumberGeneratorThread(threading.Thread):
    def __init__(self, start_number, end_number, result_list):
        threading.Thread.__init__(self)
        self.start_number = start_number
        self.end_number = end_number
        self.result_list = result_list

    def run(self):
        for i in range(self.start_number, self.end_number):
            self.result_list.append(i)


result_list = []

threads = []
for i in range(10):
    start_number = i * 10000 + 1
    end_number = (i + 1) * 10000 + 1
    thread = NumberGeneratorThread(start_number, end_number, result_list)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(result_list)
