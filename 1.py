#Прочитать файл и создать папки из внетреннего массива внутри папки temp

#Прочитать файл
import json
import os
  
# with open("new.json", "r") as f:
#     data = json.load(f)
#     print(data)
#
#
# try:
#     os.mkdir("temp")
# except:
#     pass
#
# print(data["dirs"])
#
# for i in data["dirs"]:
#     print(i, type(i))
#     print(i["name"])
#     os.mkdir("temp/" + i["name"])


n = int(input())
nums = list(map(int, input().split()))
dict1 = dict()
for i in range(len(nums)):
    if nums[i] not in dict1:
        dict1[nums[i]] = 1
    else:
        dict1[nums[i]] += 1
    print(dict1)
    keys = sorted(dict1.keys())
    for j in range(1, len(keys)):
        if keys[j] == keys[j-1] - 1:
            # asw = nums[i]
            print(i+1)
            break