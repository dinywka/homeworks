# #29
# class NewClass:
#     def __init__(self, text):
#         self.text = text
#
#     def set_text(self, text = None):
#         if text is not None:
#             self.text = text
#         else:
#             self.text = ""
#
# class ChildClass(NewClass):
#     def __init__(self, text, num):
#         super().__init__(text)
#         self.num = num
#
# main_obj = NewClass("Main")
# main_obj.set_text("New text")
# print(main_obj.text)
#
# child_obj = ChildClass("text", 56)
# child_obj.set_text("Newest text")
# print(child_obj.text)
# print(child_obj.num)
#
# #30
# class BaseClass:
#     def __init__(self, text):
#         self._text = text
#
#     def setText(self, text=None):
#         if text is not None:
#             self._text = text
#
#
# class SubClass(BaseClass):
#     def __init__(self, text, number):
#         super().__init__(text)
#         self._number = number
#
#     def setNumber(self, number):
#         self._number = number
#
#     def setText(self, text=None):
#         if text is not None:
#             self._text = text + " (modified by SubClass)"
#         else:
#             self._text = self._text + " (modified by SubClass)"
#
#
# base = BaseClass("Hello")
# print(base._text)
# base.setText("Hi")
# print(base._text)
#
# sub = SubClass("Hello", 123)
# print(sub._text)
# print(sub._number)
# sub.setText("Hi")
# print(sub._text)
# sub.setNumber(456)
# print(sub._number)

#34
class Roman:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def __add__(self, other):
        return Roman(Roman.to_roman(Roman.from_roman(self.value) + Roman.from_roman(other.value)))

    def __sub__(self, other):
        return Roman(Roman.to_roman(Roman.from_roman(self.value) - Roman.from_roman(other.value)))

    def __mul__(self, other):
        return Roman(Roman.to_roman(Roman.from_roman(self.value) * Roman.from_roman(other.value)))

    def __truediv__(self, other):
        return Roman(Roman.to_roman(Roman.from_roman(self.value) // Roman.from_roman(other.value)))

    @staticmethod
    def from_roman(s):
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(s)):
            if i > 0 and roman_dict[s[i]] > roman_dict[s[i - 1]]:
                result += roman_dict[s[i]] - 2 * roman_dict[s[i - 1]]
            else:
                result += roman_dict[s[i]]
        return result

    @staticmethod
    def to_roman(n):
        roman_dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X',
                      9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        result = ''
        for r, val in roman_dict.items():
            while n >= r:
                result += val
                n -= r
        return result

num1 = Roman("X")
num2 = Roman("XI")
print(num1+num2)
