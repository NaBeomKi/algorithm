a, b, c = map(int, open(0))
for i in range(10):
    print(str(a * b * c).count(str(i)))

# exec("n,m=0,1" + "*int(input())" * 3 + ";print(str(m).count(str(n)));n+=1" * 10)
# 위 코드는 아래의 코드가 된다.
# n, m = 0, 1 * int(input()) * int(input()) * int(input())

# print(str(m).count(str(n)))
# n += 1
# print(str(m).count(str(n)))
# n += 1
# print(str(m).count(str(n)))
# n += 1
# print(str(m).count(str(n)))
# n += 1
# print(str(m).count(str(n)))
# n += 1
# print(str(m).count(str(n)))
# n += 1
# print(str(m).count(str(n)))
# n += 1
# print(str(m).count(str(n)))
# n += 1
# print(str(m).count(str(n)))
# n += 1
# print(str(m).count(str(n)))
# n += 1
