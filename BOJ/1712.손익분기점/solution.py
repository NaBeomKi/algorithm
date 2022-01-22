a, b, c = map(int, input().split())
print((a // (c - b)) + 1 if c > b else -1)

# -a-bx-cx > 0
# 위 수식을 고치면 x > a/(c-b)
# 결론: c-b<=0 이면 절대로 손익분기점을 넘을 수 없음. c-b>0 이면 a//(c-b)+1이 x

# a, b, c = map(int, input().split())
# print(-(c <= b) or a // (c - b) + 1)
