#Разработать декоратор для проверки наличия в входном аргументе пароля, т.е. decorator_authentificator.

def decorator_authentificator(func):
    def wrapper(password, *args, **kwargs):
        if password == "strong_password":
            return func(password, *args, **kwargs)
        else:
            return ("Wrong password!")
    return wrapper


@decorator_authentificator
def password_to_check(password):
    return ("Valid password!")

print(password_to_check("strong_password"))


#2
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

    print(password_to_check("strong_password"))


