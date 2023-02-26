#1
import re
import datetime

password = input("Введите пароль: ")
email = input("Введите email: ")
def pass_checker(password:str, email: str):

    result = 0
    if re.match(r"^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", string=password):
        print("Valid password!")
        result += 1 
    else:
        print("Invalid password!")
    
    if re.match(r"[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", string=email):
        print("Valid email!")
        result += 1
    else: 
        print("Invalid email!")

    if result == 2:
        now1 = datetime.datetime.now()
        now2 = now1.strftime("%d-%m-%y")
        with open ("new_pass.txt", "w") as file1:
            file1.writelines([now2,"\n", password, "\n", email])
        
    
if __name__=="__main__":
    pass_checker(password, email)

#2
# import os
# import random

# def file_creator():
#     dirs = next(os.walk("."))[1]
#     ran_dirs = random.sample(dirs, 4)
#     for dir in ran_dirs:
#         file_path = os.path.join(dir, "мусор.json")
#         with open(file_path, "w") as f:
#             f.write("This file to delete!")

# def file_cleaner():
#     dirs = os.getcwd()
#     print(dirs)
#     name = "мусор.json"
#     for roots, dirs, files in os.walk(dirs):
#         for file in files:
#             file_path = os.path.join(roots, name)
#             if os.path.exists(file_path):
#                 os.remove(file_path)


# if __name__=="__main__":
    # file_creator()
    # file_cleaner()