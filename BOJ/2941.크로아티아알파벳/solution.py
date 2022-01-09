string = input()
char_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for i in char_list:
    string = string.replace(i, "a")
print(len(string))

# import re

# print(len(re.sub("dz=|[ln]j|\w\W", "Z", input())))

# 정규식 연산: re - https://docs.python.org/ko/3/library/re.html
# sub - https://docs.python.org/ko/3/library/re.html#re.sub
