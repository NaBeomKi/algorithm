def solution(arr):
    min_num = min(arr)
    answer = [i for i in arr if i != min_num]
    return answer if answer else [-1]


# answer = [i for i in arr if i != min(arr)]
# 이 경우 매번 min함수를 사용하며 시간초과가 발생
# https://programmers.co.kr/questions/4949
