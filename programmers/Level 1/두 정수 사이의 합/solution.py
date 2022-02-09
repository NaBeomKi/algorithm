def solution(a, b):
    m, n = min(a, b), max(a, b)
    return sum(i for i in range(m, n + 1))


# def solution(a, b):
#     if a > b:
#         a, b = b, a
#     return sum(range(a, b + 1))

# def solution(a, b):
#     return (abs(a - b) + 1) * (a + b) // 2
