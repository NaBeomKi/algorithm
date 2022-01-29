data = input()
result_str = []
result_num = 0
for i in data:
    if ord(i) >= ord("A") and ord(i) <= ord("Z"):
        result_str.append(i)
    else:
        result_num += int(i)
result_str.sort()
if not result_num:
    result_str.append(str(result_num))
print("".join(result_str))

# data = input()
# result_str = []
# result_num = 0
# for i in data:
#     if i.isalpha():
#         result_str.append(i)
#     else:
#         result_num += int(i)
# result_str.sort()
# if not result_num:
#     result_str.append(str(result_num))
# print("".join(result_str) + str(result_num))
