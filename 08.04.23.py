#35
# def summing(num1, num2: int) -> int:
#     try:
#         return num1+num2
#     except TypeError:
#         return "Ожидаемый тип данных — число!"
#
# if __name__ == "__main__":
#     print(summing(2, "n"))

#36
my_list = [1, 2, 3]

try:
    index = int(input("Введите индекс элемента списка: "))
    print(f"Элемент списка с индексом {index}: {my_list[index]}")
except IndexError:
    print("Ошибка: индекс выходит за границы списка.")
except ValueError:
    print("Ошибка: введенный индекс не является числом.")
