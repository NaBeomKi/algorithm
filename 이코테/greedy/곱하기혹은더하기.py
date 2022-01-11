n = input()
result = 0
for i in n:
    i = int(i)
    if result == 0 or result == 1 or i == 0 or i == 1:
        result += i
        continue
    result *= i
print(result)

# data = input()
# result = int(data[0])
# for i in range(1, len(data)):
#     num = int(data[i])
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         result *= num
# print(result)
