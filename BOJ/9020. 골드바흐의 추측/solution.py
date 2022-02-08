def is_prime(n):
    if n <= 1:
        return False
    for j in range(2, int(n ** 0.5) + 1):
        if not n % j:
            return False
    return True


for n in map(int, [*open(0)][1:]):
    for i in range(n // 2, 1, -1):
        if is_prime(i) and is_prime(n - i):
            print(i, n - i)
            break

# 골드바흐의 추측 - https://velog.io/@warmwhiten/%EB%B0%B1%EC%A4%80-9020-%EA%B3%A8%EB%93%9C%EB%B0%94%ED%9D%90%EC%9D%98-%EC%B6%94%EC%B8%A1

# (*p,) = range(5 ** 6)
# for i in p[2:]:
#     for j in p[2 * i :: i]:
#         p[j] = 0
# S = set(p[2:])
# exec(
#     int(input())
#     * "n=int(input())\nfor i in p[n//2:]:\n if i*(n-i in S):print(n-i,i);break\n"
# )
