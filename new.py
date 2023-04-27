import sys

# a = (2, 3, "a")
# b = [2, 3, "a"]
#
# print(sys.getsizeof(a))
# print(sys.getsizeof(b))

# str1 = "qwe"
# str2 = "rty"
# print(str1+str2)
#
# str3 = "Hi"
# num1 = 234
#
# print(f'{str3}, {num1}')
# print('{}, {}'.format(str3, num1))

# lst1 = [1, 2, 3]
# lst1.insert(4, 2)
# lst2 = [4, 5, 6]
# print([*lst1, *lst2])

# dict1 = {"name": "Dina", "age": 34}
# print(dict1["name"])
# print(dict1.get("name1", "Python"))

# import re
# def check_email(func):
#     def wrapper(*args, **kwargs):
#         regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
#         if not re.search(regex, args[0]):
#             raise Exception("Invalid email!")
#         return func(*args, **kwargs)
#     return wrapper
#
# @check_email
# def auth(email, password):
#     return email + "|" + password
# print(auth("dinamail.ru", "123"))
# print(auth("dina@mail.ru", "123"))

# from typing import Union
# def sum(a: int|float, b: Union[int, float]) -> float:
#     return a + b
# print(sum(12, 13)/10)

# str1 = "qwe"
# str1[-1] = "10"
#
# arr = [1, 2, 3, 2]
#
# print(arr.remove(2))
# print(arr)
# del arr[1]
# print(arr)
# # print(arr.pop())

# arr = ["apple", "orange", "grape"]
# # str1 = ', '.join(arr)
# # print(str1)
# str1 = ''
#
# for i in arr:
#     str1 += str(i) + ", "
# print(str1[:-2])

# elem1 = 14
# elem = [12, 13]
# print(elem1 in elem)





