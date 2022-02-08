h, m = map(int, input().split())
time2min = 24 * 60 + m if h == 0 and m < 45 else h * 60 + m
alert_min = time2min - 45
print(alert_min // 60, alert_min % 60)

# a, b = map(int, input().split())
# print((a - (b < 45)) % 24, (b - 45) % 60)

# 모듈러 연산이란?
# https://ko.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/what-is-modular-arithmetic
