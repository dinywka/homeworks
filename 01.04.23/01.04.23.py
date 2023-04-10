# #22
# #1
# def superset(set1, set2):
#     if set1 == set2:
#         print("Множества равны")
#     elif set1.issuperset(set2):
#         print(f"Объект {set1} является чистым супермножеством")
#     else:
#         print("Супермножество не обнаружено")
#
# supset = {1, 2, 3, 4}
# set1 = {1, 2}
# if __name__ == "__main__":
#     superset(supset, set1)
#
# #2
# dictionary = {}
#
# def add_word():
#     en_word = input("Введите слово на английском: ")
#     fr_word = input("Введите перевод на французский: ")
#     dictionary[en_word] = fr_word
#     print(f"Слово {en_word} добавлено в словарь.")
#
# def remove_word():
#     en_word = input("Введите слово на английском, которое нужно удалить: ")
#     if en_word in dictionary:
#         del dictionary[en_word]
#         print(f"Слово {en_word} удалено из словаря.")
#     else:
#         print(f"Слово {en_word} не найдено в словаре.")
#
# def search_word():
#     en_word = input("Введите слово на английском для поиска перевода: ")
#     if en_word in dictionary:
#         print(f"Перевод слова {en_word} на французский: {dictionary[en_word]}")
#     else:
#         print(f"Слово {en_word} не найдено в словаре.")
#
# def replace_word():
#     en_word = input("Введите слово на английском, которое нужно заменить: ")
#     if en_word in dictionary:
#         fr_word = input(f"Введите новый перевод слова {en_word} на французский: ")
#         dictionary[en_word] = fr_word
#         print(f"Перевод слова {en_word} обновлен.")
#     else:
#         print(f"Слово {en_word} не найдено в словаре.")
#
# def show_menu():
#     print("1. Добавить слово в словарь")
#     print("2. Удалить слово из словаря")
#     print("3. Поиск перевода слова")
#     print("4. Замена перевода слова")
#     print("5. Выйти из программы")
#
# while True:
#     show_menu()
#     choice = input("Введите номер выбранного пункта: ")
#     if choice == '1':
#         add_word()
#     elif choice == '2':
#         remove_word()
#     elif choice == '3':
#         search_word()
#     elif choice == '4':
#         replace_word()
#     elif choice == '5':
#         break
#     else:
#         print("Неправильный выбор. Попробуйте еще раз.")
#
# if __name__ == "__main__":
#     show_menu()

#3
# def set_gen(numbers):
#     result = set()
#     count = {}
#     for n in numbers:
#         if n not in count:
#             result.add(n)
#             count[n] = 1
#         else:
#             count[n] += 1
#             result.add(str(n) * count[n])
#     return result
#
# nums = [1, 2, 3, 444, 3, 2]
# if __name__ == "__main__":
#     print(set_gen(nums))

#23
#1
# def biggest_dict(**kwargs):
#     if len(kwargs) > 0:
#         global my_dict
#         if 'first_one' not in my_dict:
#             my_dict['first_one'] = 'we can do it'
#         for key, value in kwargs.items():
#             my_dict[key] = value
#     return my_dict
#
# my_dict = {'first_one': 'we can do it'}
# if __name__ == "__main__":
#     print(biggest_dict(one = 1, two = 2))

#2
# my_dict = {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 5}
#
# keys = list(my_dict.keys())
# my_dict[keys[-1]], my_dict[keys[0]] = my_dict[keys[0]], my_dict[keys[-1]]
#
# my_dict.pop(keys[1])
#
# my_dict.update({'new_key': 'new_value'})
#
# print(my_dict)

#3
# def add_country(countries):
#     country_name = input("Введите название страны: ")
#     capital_name = input("Введите название столицы: ")
#     countries[country_name] = capital_name
#     print(f"Страна {country_name} успешно добавлена в словарь")
#
# def delete_country(countries):
#     country_name = input("Введите название страны: ")
#     if country_name in countries:
#         del countries[country_name]
#         print(f"Страна {country_name} успешно удалена из словаря")
#     else:
#         print(f"Страна {country_name} не найдена в словаре")
#
# def find_country(countries):
#     country_name = input("Введите название страны: ")
#     if country_name in countries:
#         print(f"Столица страны {country_name} - {countries[country_name]}")
#     else:
#         print(f"Страна {country_name} не найдена в словаре")
#
# def edit_country(countries):
#     country_name = input("Введите название страны: ")
#     if country_name in countries:
#         capital_name = input("Введите новое название столицы: ")
#         countries[country_name] = capital_name
#         print(f"Столица страны {country_name} успешно изменена на {capital_name}")
#     else:
#         print(f"Страна {country_name} не найдена в словаре")
#
# def save_countries(countries):
#     with open("countries.txt", "w") as f:
#         for country, capital in countries.items():
#             f.write(f"{country}:{capital}\n")
#     print("Данные успешно сохранены в файл")
#
# def load_countries():
#     countries = {}
#     try:
#         with open("countries.txt", "r") as f:
#             for line in f:
#                 country, capital = line.strip().split(":")
#                 countries[country] = capital
#         print("Данные успешно загружены из файла")
#         return countries
#     except FileNotFoundError:
#         print("Файл не найден")
#         return {}
#
# def main():
#     countries = load_countries()
#
#     while True:
#         print("\nВыберите действие:\n1. Добавить страну\n2. Удалить страну\n3. Найти страну\n4. Редактировать страну\n5. Сохранить данные\n6. Выйти")
#         choice = input("Введите номер действия: ")
#
#         if choice == "1":
#             add_country(countries)
#         elif choice == "2":
#             delete_country(countries)
#         elif choice == "3":
#             find_country(countries)
#         elif choice == "4":
#             edit_country(countries)
#         elif choice == "5":
#             save_countries(countries)
#         elif choice == "6":
#             print("Выход из программы")
#             break
#         else:
#             print("Некорректный ввод, повторите попытку")
#
# if __name__ == "__main__":
#     main()

#24
#1
import datetime
#
# date = datetime.date(2015, 6, 16)
# week_number = date.strftime("%U")
#
# print(week_number)

#2
# year = 2015
# week_number = 50
# first_day = datetime.date(year, 1, 1)
# first_monday = first_day + datetime.timedelta(days=(0 - first_day.weekday()) % 7)
# current_monday = first_monday + datetime.timedelta(days=7 * (week_number - 1))
# date = current_monday + datetime.timedelta(days=(datetime.date(year, 1, 1).weekday() - current_monday.weekday()) % 7)
#
# print(date.strftime('%a %d %B %H:%M:%S %Y'))

#3
# year = 2022
#
# sundays = []
# for month in range(1, 13):
#     for day in range(1, 32):
#         try:
#             date = datetime.date(year, month, day)
#             if date.weekday() == 6:
#                 sundays.append(date)
#         except ValueError:
#             pass
#
# for sunday in sundays:
#     print(sunday)

#4
import datetime

def addYears(date_obj, years):
    try:
        new_date = date_obj.replace(year = date_obj.year + years)
    except ValueError:
        new_date = date_obj + (datetime.date(date_obj.year + years, 1, 1) - datetime.date(date_obj.year, 1, 1))
    return new_date
if __name__=="__main__":
    print(addYears(datetime.date(2015, 1, 1), -1))
    print(addYears(datetime.date(2015, 1, 1), 0))
    print(addYears(datetime.date(2015, 1, 1), 2))
    print(addYears(datetime.date(2000, 2, 29), 1))
