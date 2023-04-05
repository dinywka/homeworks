#19
#1
def calculate_min_cost(n, prices):
    prices.sort(reverse=True)
    min_cost = sum(prices)

    for i in range(2, n, 3):
        min_cost -= prices[i]

    return min_cost

print(calculate_min_cost(6, [1, 5, 4,3, 5, 7]))

#2
def find_closest_numbers(numbers):
    numbers.sort()
    min_diff = float('inf')
    closest_pair = None

    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i-1]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i-1], numbers[i])

    return closest_pair

nums = [9, 4, 1, 6]
print(find_closest_numbers(nums))

#20
#1
def align_strings(strings):
    max_len = max(len(s) for s in strings)
    aligned_strings = []
    for s in strings:
        aligned_s = '*' * (max_len - len(s)) + s
        aligned_strings.append(aligned_s)
    return aligned_strings

words = ["da", "net", "poka"]
print(align_strings(words))

#2
def add_element_to_array(arr):
    positive_sum = sum(filter(lambda x: x > 0, arr))
    negative_sum = sum(filter(lambda x: x < 0, arr))
    new_element = abs(negative_sum) - positive_sum
    arr.append(new_element)
    return new_element

myarr = [-3,-2,1,2,3,4]
print(add_element_to_array(myarr))

#21
#1
class Decoder:
    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, text):
        encrypted_text = ""
        for i in text:
            if i.isalpha():
                char = ord(i) + self.shift
                if i.isupper():
                    if char > ord('Z'):
                        char -= 26
                    elif char < ord("A"):
                        char += 26
                else:
                    if char > ord("z"):
                        char -= 26
                    elif char < ord("a"):
                        char += 26
                encrypted_text += chr(char)
            else:
                encrypted_text += i
        return encrypted_text

    def decode(self, encrypted_text):
        text = ""
        for i in encrypted_text:
            if i.isalpha():
                char = ord(i) - self.shift
                if i.isupper():
                    if char > ord('Z'):
                        char -= 26
                    elif char < ord("A"):
                        char += 26
                else:
                    if char > ord("z"):
                        char -= 26
                    elif char < ord("a"):
                        char += 26
                text += chr(char)
            else:
                text += i
        return text


if __name__ == "__main__":
    to_code = Decoder(3)
    decoded = to_code.encrypt("Hi! My name is Dina!")
    print(decoded)
    print(to_code.decode(decoded))

#2
# fruits = ('яблоко', 'банан', 'киви', 'апельсин', 'яблоко', 'груша', 'яблоко')
# fruit = input('Введите название фрукта: ')
# count = fruits.count(fruit)
# print(f'Фрукт {fruit} встречается в кортеже {count} раз(а)')

#3
fruits = ('apple', 'banana', 'orange', 'mango', 'apple', 'banana', 'banana', 'strawberry-banana', 'mango', 'banana-mango')
fruit_name = input('Введите название фрукта: ')
count_partial = sum(1 for fruit in fruits if fruit_name in fruit)
print(f"Фрукт '{fruit_name}' встречается {count_partial} раз(а) как часть элемента")

#4
car_brands = ('Toyota', 'Nissan', 'Honda', 'Ford', 'Chevrolet', 'Honda', 'Nissan', 'Toyota')

old_brand = input('Введите название производителя для замены: ')
new_brand = input('Введите новое название производителя: ')

new_car_brands = tuple(new_brand if brand == old_brand else brand for brand in car_brands)

print(new_car_brands)
