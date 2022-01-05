def getNum(s):
    # return "0"+num if len(num:=input())==1 else num
    return "0" + s if len(s) == 1 else s


# start = current = "0"+num if len(num:=input())==1 else num
start = current = getNum(input())
i = 0
while current != start or not i:
    a, b = current
    # x,y = "0"+new_num if len(new_num:=str(int(a)+int(b)))==1 else new_num
    x, y = getNum(str(int(a) + int(b)))
    current = b + y
    i += 1
print(i)

# 바다코끼리 연산자를 사용할 수도 있지만, 따로 함수로 빼낸 상태에서는 없어도 그만이라 제외

# a = n = int(input())
# c = 1
# while (a := a % 10 * 10 + a * 11 // 10 % 10) - n:
#     c += 1
# print(c)

# a * 11 // 10 % 10
# 두자리 숫자에 11을 곱하면 십의 자리 숫자는 각 자릿수의 합이 된다
# ex) 26 * 11 = 286, 99 * 11 = 1089, 71 * 11 = 781, 9 * 11 = 99
