def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))


# key를 여러개 주기 위해 tuple 사용
# https://codingpractices.tistory.com/57
