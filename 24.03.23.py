# #1
# import tkinter as tk
# import time
#
# class Calculator:
#     def __init__(self):
#         self.window = tk.Tk()
#         self.window.title("Calculator")
#         self.window.geometry("350x450")
#         self.entry = tk.Entry(self.window, width=35, justify="right")
#         self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
#
#         self.buttons = (('7', '8', '9', '/'),
#                         ('4', '5', '6', '*'),
#                         ('1', '2', '3', '-'),
#                         ('0', '.', '=', '+'),
#                         ('C'))
#
#         for row, but_row in enumerate(self.buttons, 1):
#             for col, but_text in enumerate(but_row):
#                 button = tk.Button(self.window, text=but_text, width=5, height=4, command=
#                                    lambda text=but_text: self.but_click(text))
#                 button.grid(row=row, column=col)
#
#     def but_click(self, text):
#         if text == "=":
#             try:
#                 result = eval(self.entry.get())
#                 self.entry.delete(0, tk.END)
#                 self.entry.insert(tk.END, result)
#             except:
#                 self.entry.delete(0, tk.END)
#         elif text == 'C':
#             self.entry.delete(0, tk.END)
#         else:
#             self.entry.insert(tk.END, text)
#
#     def run(self):
#         self.window.mainloop()
#
# if __name__ == '__main__':
#     calculator = Calculator()
#     calculator.run()

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


#12
#1
# s=input()
# s1 = s.split()
# print(str(s1[1]+" "+s1[0]))

#2
# s=input()
# x=s.count(" ")
# print(x+1)

#3
# s=input()
# ng=s.replace("2020", "2021")
# print(ng)


#13
# x = int(input())
# s=x
# sq=0+abs(x**2)
#
# while s!=0:
#     x=int(input())
#     s+=x
#     sq=sq+abs(x)**2
#     if s==0:
#         break
# print(sq)

#14
# marks = input().split()
#
# count_2 = marks.count('2')
# count_3 = marks.count('3')
# count_4 = marks.count('4')
# count_5 = marks.count('5')
#
# average_mark = sum(map(int, marks)) / len(marks)
#
# print(f"{count_5} {count_4} {count_3} {count_2}")
# print(f"{average_mark:.9f}")

#15
# marks = input().split()
# new_marks = []
# for i in marks:
#     if i == "2":
#         i = 3
#     new_marks.append(str(i))
# print(new_marks)
