#1

import json
import requests
import aiohttp
import asyncio

# def sync_download_json():
#     for i in range(1, 10 + 1):
#         with open(f"new.json{i}", "w") as f:
#             r = requests.get(f"https://jsonplaceholder.typicode.com/todos/{i}")
#             data = r.json()
#             str_data = json.dumps(data)
#             f.write(str_data)
#
# sync_download_json()
#
# def threading_download_mass_json():
#     new_thread_list = []
#     for i in range(1, 10 + 1):
#         new_thread_list.append(threading.Thread(target=sync_download_json, args=(), kwargs={}))
#     for i in new_thread_list:
#         i.start()
#     for i in new_thread_list:
#         i.join()
#
# def processing_download_mass_json():
#     new_process_list = []
#     for i in range(1, 50 + 1):
#         new_process_list.append(multiprocessing.Process(target=sync_download_json, args=(), kwargs={}))
#     for i in new_process_list:
#         i.start()
#     for i in new_process_list:
#         i.join()


# async def async_download_json():
#     async with aiohttp.ClientSession() as session:
#         for i in range(1, 11):
#             async with session.get(f"http://jsonplaceholder.typicode.com/todos/{i}", ssl=False) as response:
#                 data = await response.json()
#                 str_data = json.dumps(data)
#                 with open(f"new.json{i}", "w") as f:
#                     f.write(str_data)

# asyncio.run(async_download_json())

# if __name__ == "__main__":
#     sync_download_json()
#     threading_download_mass_json()
#     processing_download_mass_json()
#     asyncio.run(async_download_json())

#4
#1
def triangle_check(a, b, c: int):
    return a+b>c and a+c>b and b+c>a

#2
# a = int(input())
def odd_even(a: int):
    return a % 2 == 0

#3
def sum_check(a, b, c: int):
 return a+b>c

#4
def num_compare(a, b: int):
    return a>b

if __name__ == "__main__":
    print(triangle_check(4, 5, 6))
    print(odd_even(2))
    print(sum_check(4, 5, 6))
    print(num_compare(4, 3))


#5
#1
login = input("Enter login:")
password = input("Enter password:")

if password == "qwerty" and login == "user":
    print("Authentication comleted")
else:
    print("Invalid login or password")

#2
x = int(input("Insert amount in KZT:"))
cur = int(input("Choose currency:\n[1]USD\n[2]EUR\n[3]RUB\n"))
if cur == 1:
    x=round(x/420, 2)
    print(x, "USD")
elif cur == 2:
    x=round(x/510, 2)
    print(x, "EUR")
elif cur == 3:
    x=round(x/5.8, 2)
    print(x, "RUB")
else:
    print("Invalid currency")