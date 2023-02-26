#1.1
# def is_palindrome(rec_str: str):
#     strr = "".join(["".join(filter(str.isalpha, w)) for w in rec_str]).lower()
#     if len(strr) < 1:
#         return ("Палиндром!")
#     else:
#         if strr[0] == strr[-1]:
#             return is_palindrome(strr[1:-1])
#         else:
#             return ("Не палиндром!")
#1.2
# def is_palindrome(rec_str: str):
#     strr = "".join(["".join(filter(str.isalpha, w)) for w in rec_str]).lower()
#     if strr == strr[::-1]:
#         return ("Палиндром!")
#     else:
#         return ("Не палиндром!")

#1.3
def is_palindrome(rec_str: str):
    left = 0
    right = len(rec_str) - 1
    while left < right:
        while left < right and not rec_str[left].isalnum():
            left +=1
        while left < right and not rec_str[right].isalnum():
            right -= 1
        if rec_str[left].lower() != rec_str[right].lower():
            return ("Не палиндром!")
        left += 1
        right -= 1
    return ("Палиндром!")

if __name__ == "__main__":
    print(is_palindrome('madam, I\'m Adam'))


#2
# def for_str(listt: list) -> str:
#     listt = sorted(listt)
#     fin_str = ""
#     start = listt[0]
#     end = listt[0]
#     for i in range(1, len(listt)):
#         if listt[i] == end + 1:
#             end = listt[i]
#         else:
#             if start == end:
#                 fin_str += str(start) + ","
#             else:
#                 fin_str += str(start) + "-" + str(end) + ","
#             start = listt[i]
#             end = listt[i]

#     if start == end:
#         fin_str += str(start)
#     else:
#         fin_str += str(start) + "-" + str(end)
#     return fin_str

# if __name__ == "__main__":
#     print(for_str([1, 3, 4]))
