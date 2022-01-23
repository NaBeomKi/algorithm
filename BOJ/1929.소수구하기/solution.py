m, n = map(int, input().split())
bool_list = [True] * (n + 1)
for i in range(2):
    bool_list[i] = False
for i in range(2, int(n ** 0.5) + 1):
    if bool_list[i]:
        for j in range(i + i, n + 1, i):
            bool_list[j] = False
print(*[i for i in range(m, n + 1) if bool_list[i]], sep="\n")

# 에라토스테네스의 체 - https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4

# m, n = map(int, input().split())
# l = [*range(n + 1)]
# for i in l:
#     if 1 < i:
#         l[i * i :: i] = -(i + ~n // i) * [0]
#     if 1 < i >= m:
#         print(i)
