count = 0
for i in range(1, int(input()) + 1):
    if i < 100:
        count += 1
    else:
        a, b, c, *_ = map(int, str(i))
        count += a - b == b - c
print(count)

# 문제 접근 방법과 풀이 https://ooyoung.tistory.com/65

# print(
#     sum(
#         i < 100 or i // 100 * 21 + i == i // 10 * 12
#         for i in range(1, int(input()) + 1)
#     )
# )

# 각 자릿수가 등차수열이 되는 관계를 수식으로 정리해 나온 결과 https://www.acmicpc.net/board/view/79533
#########################################################

# n = int(input())
# print(
#     n * (n < 100)
#     or n // 105 * 5 + min(n % 105 - n // 105 % 2 * 6, 48) // 12 + 95
# )
