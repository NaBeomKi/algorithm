def solution(x, n):
    return [i for i in range(x, x * (n + 1), x)]


# 아래가 더 맞는 코드라고 생각한다. 위의 경우 쓸데없이 낭비되는 반복 횟수가 있음

# def solution(x, n):
#     return [i * x + x for i in range(n)]
