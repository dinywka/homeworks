#2103. Rings and Rods
# def countPoints(rings: str):
#     r_dict = dict()
#     result = []
#     for i in range(0, len(rings)-1, 2):
#         if rings[i+1] not in r_dict:
#             r_dict[rings[i+1]] = rings[i]
#         else:
#             r_dict[rings[i+1]] += rings[i]
#     for k, v in r_dict.items():
#         if ("B" in v) and ("R" in v) and ("G" in v):
#             result.append(int(k))
#     if result:
#         return result
#     else:
#         return 0
#
# rings = "B0B6G0R6R0R6G9"
# print(countPoints(rings))

#136. Single Number

#136. Single Number
# def singleNumber(nums):
#     for i in nums:
#         if nums.count(i) == 1:
#             return i
#
# nums = [0,1,0,1,0,1,99]
# print(singleNumber(nums))

