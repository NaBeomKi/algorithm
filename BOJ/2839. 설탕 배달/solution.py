n = int(input())
result = 0
while n >= 0:
    if not n % 5:
        result += n // 5
        break
    n -= 3
    result += 1
print(-1 if n < 0 else result)

# 참고 - https://reakwon.tistory.com/126

# n = int(input())
# print(-(n in [4, 7]) or n - 2 * n // 5 * 2)

# 참고 - https://www.acmicpc.net/board/view/80893
