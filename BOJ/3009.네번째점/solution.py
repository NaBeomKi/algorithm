x1, y1, x2, y2, x3, y3 = map(int, open(0).read().split())
x = (x1, x2, x3)
y = (y1, y2, y3)
x_set = list(set(x))
y_set = list(set(y))
result_x = 0
result_y = 0
for i in range(2):
    if x.count(x_set[i]) == 1:
        result_x = x_set[i]
    if y.count(y_set[i]) == 1:
        result_y = y_set[i]
print(result_x, result_y)


x = y = 0
exec("a,b=map(int,input().split());x^=a;y^=b;" * 3)
print(x, y)

# ^: XOR 연산자
# https://www.acmicpc.net/board/view/74274
# 코딩 도장 - 47.1 비트 연산자 사용하기
# https://dojang.io/mod/page/view.php?id=2460
