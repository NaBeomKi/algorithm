text_list = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
result = 0
for char in input():
    for i in range(len(text_list)):
        if text_list[i].count(char):
            result += i + 3
            break
print(result)

# print(sum(5 * min(ord(x), 88) // 16 - 17 for x in input()))
