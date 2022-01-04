count = int(input())
for i in range(0, count):
    a, b = map(int, input().split())
    print(a + b)

# for a, _, c, _ in [*open(0)][1:]:
#     print(int(a) + int(c))

# [*open(0)]와 list(open(0))는 동일
# 문제의 입력 값을 입력하면 아래가 된다.
# ['5\n', '1 1\n', '2 3\n', '3 4\n', '9 5\n', '2 6\n']

# 파이썬의 Asterisk(*) 이해하기
# https://mingrammer.com/understanding-the-asterisk-of-python/
