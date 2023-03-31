#1
# import PyQt6
# import tkinter as tk
# import time
#
# from PyQt6 import QtWidgets, QtCore, QtGui, uic
#
# class Window(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.ui = uic.loadUi("28.ui", self)
#         self.label = self.ui.label
#         self.label.setText("")
#         self.buttons = [getattr(self.ui, f"pushButton_{i}") for i in range(2, 18)]
#         for button in self.buttons:
#             button.clicked.connect(self.but_click)
#
#     def but_click(self):
#         button = self.sender()
#         text = button.text()
#
#         if text == "=":
#             try:
#                 result = eval(self.label.text())
#                 self.label.setText(str(result))
#             except:
#                 self.label.setText("Error")
#         elif text == 'C':
#             self.label.setText("")
#         else:
#             self.label.setText(self.label.text() + text)
#
# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])
#     window = Window()
#     window.show()
#     app.exec()


#2
# class Timer:
#     def __init__(self):
#         self.window = tk.Tk()
#         self.window.title("Timer")
#         # self.window.geometry("450*400")
#         self.label = tk.Label(text="00:00:00")
#         self.label.pack()
#         self.start_but = tk.Button(self.window, text='Start', width=7, height=4, command=self.start_timerun)
#         self.start_but.pack(side='left')
#         self.stop_but = tk.Button(self.window, text='Stop', width=7, height=4, command=self.stop_timerun)
#         self.stop_but.pack(side='right')
#         self.reset_but = tk.Button(self.window, text='Reset', width=7, height=4, command=self.reset_timer)
#         self.reset_but.pack(side='right')
#         self.timer_work = False
#         self.seconds = 0
#         self.minutes = 0
#         self.hours = 0
#         self.time = '00:00:00'
#
#     def stop_timerun(self):
#         self.timer_work = False
#         self.seconds = 0
#         self.minutes = 0
#         self.hours = 0
#         self.update_label()
#
#     def reset_timer(self):
#         self.timer_work = False
#         self.seconds = 0
#         self.minutes = 0
#         self.hours = 0
#         self.label.config(text="00:00:00")
#
#     def start_timerun(self):
#         if self.timer_work == False:
#             self.timer_work = True
#             self.timer_run()
#
#     def stop_timerun(self):
#         self.timer_work = False
#
#     def timer_run(self):
#         if self.timer_work:
#             self.seconds += 1
#             if self.seconds == 60:
#                 self.minutes += 1
#                 self.seconds = 0
#             if self.minutes == 60:
#                 self.hours += 1
#                 self.minutes = 0
#         self.update()
#
#     def update(self):
#         timer_text = f"{self.hours}:{self.minutes}:{self.seconds}"
#         self.label.config(text=timer_text)
#         if self.timer_work:
#             self.label.after(1000, self.timer_run)
#
#
#     def run(self):
#         self.window.mainloop()
#
# if __name__ == '__main__':
#     timer = Timer()
#     timer.run()


#15
#1
# def lst(*args):
#     sch=0
#     sn=0
#     for i in args:
#         if i%2==0:
#             sch+=1
#         elif i%2!=0:
#             sn+=1
#     if sn>sch:
#         print("Нет")
#     else:
#         print("Да")

# lst(4, 16, 19, 31, 2)

#2
# def mass():
#     a=[]
#     r=1
#     s=0
#     for i in range(3):
#         a.append([])
#         for j in range(3):
#             a[i].append(r)
#             r+=1
#     for i in a:
#         for j in i:
#             print(j, end=' ')
#         print()
#     for i in range(3):
#         s+=a[i][i]
#     print(s)
#
# mass()

#3
# def cv(name, date, university, work):
#     print(f"Name: {name}")
#     print(f"Date of birth: {date}")
#     print(f"Education:{university}")
#     print(f"Experience: {work}")

# cv("Dina Kulmagambetova", "28.03.1989", "kazNU", "Exante, office-manager")

#16
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# if __name__ == "__main__":
#     print(fibonacci(10))

#16.2
# def is_power_of_two(n):
#     if n == 0:
#         return False
#     while n != 1:
#         if n % 2 != 0:
#             return False
#         n = n // 2
#     return True
#
# if __name__ == "__main__":
#     print(is_power_of_two(8))

#17
import math
print("1-Сложение")
print("2-Вычитание")
print("3-Умножение")
print("4-Деление")
print("5-Нахождение факториала")
print("6-нахождение фибоначчи")
print("7-Возведение в степень")
print("8-Синус")
print("9-Косинус")
print("10-Тангенс")
print("11-Аркосинус")
print("12-Арксинус")
print("13-Арктангенс")
message = int(input("Выберите функцию:"))
summ = lambda x, y: x+y
subt = lambda x, y: x-y
mult = lambda x, y: x*y
div = lambda x, y: x/y

def fact(x):
    if x==1:
        return 1
    else:
        return(x*fact(x-1))

def fib(x):
    if x<=1:
        return x
    else:
        return (fib(x-1)+fib(x-2))

deg = lambda x, y: x**y

sinn = lambda x: math.sin(math.radians(x))
coss = lambda x: math.cos(math.radians(x))
tang = lambda x: math.tan(math.radians(x))
acoss = lambda x: math.acos(math.radians(x))
asinn = lambda x: math.asin(math.radians(x))
atang = lambda x: math.atan(math.radians(x))

def calculator(message):
    x = int(input("Введите цифру"))
    if message==1 or message==2 or message==3 or message==4 or message==7:
        y = int(input("Введите цифру"))
    if message == 1:
        return summ(x, y)
    elif message == 2:
        return subt(x, y)
    elif message == 3:
        return mult(x, y)
    elif message == 4:
        return div(x, y)
    elif message == 5:
        return fact(x)
    elif message == 6:
        return fib(x)
    elif message == 7:
        return deg(x, y)
    elif message == 8:
        return sinn(x)
    elif message == 9:
        return coss(x)
    elif message == 10:
        return tang(x)
    elif message == 11:
        return acoss(x)
    elif message == 12:
        return asinn(x)
    elif message == 13:
        return atang(x)
    else:
        print("No such function. Please try again")

print(calculator(message))


#2

board = list(range(1,10))
wins_coord = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

def draw_board():
   print("-------------")
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
   print("-------------")

def take_input(player_token):
   while True:
      value = input(f"Куда поставить {player_token}?")
      if not (value in "123456789"):
         print("Ошибочный ввод. Повторите")
         continue
      value = int(value)
      if str(board[value - 1]) in "XO":
         print("Эта клетка занята")
         continue
      board[value - 1] = player_token
      break

def check_win():
   for each in wins_coord:
      if (board[each[0]-1]) == (board[each[1]-1]) == (board[each[2]-1]):
         return board[each[1]-1]
   else:
      return False

def main():
   counter=0
   while True:
      draw_board()
      if counter%2==0:
         take_input('X')
      else:
         take_input('O')
      if counter>3:
         winner=check_win()
         if winner:
            draw_board()
            print(f"{winner} выиграл")
            break
      counter +=1
      if counter>8:
         draw_board()
         print("Ничья")
         break

main()