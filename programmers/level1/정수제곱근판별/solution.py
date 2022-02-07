def solution(n):
    for i in range(1, int(n ** 0.5) + 1):
        if i * i == n:
            return (i + 1) * (i + 1)
    return -1


# def solution(n):
#     sqrt = n ** (1 / 2)
#     if sqrt % 1 == 0:
#         return (sqrt + 1) ** 2
#     return -1
