def solution(x):
    num = sum(map(int, str(x)))
    return True if not x % num else False


# 삼항연산자를 쓸 필요가 없었다.

# def solution(x):
#     return x % sum([int(c) for c in str(x)]) == 0
