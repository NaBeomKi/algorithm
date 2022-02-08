n = int(input())
data = list(map(int, input().split()))
for i in data:
    if i <= 1:
        n -= 1
        continue
    for j in range(2, int(i ** (1 / 2)) + 1):
        if not i % j:
            n -= 1
            break
print(n)

# input()
# print(
#     sum(
#         all(n % j for j in range(2, n)) * n > 1
#         for n in map(int, input().split())
#     )
# )

# all - https://docs.python.org/ko/3/library/functions.html#all
