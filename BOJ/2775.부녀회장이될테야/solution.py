for _ in range(int(input())):
    k, n = int(input()), int(input())
    floor = [i for i in range(1, n + 1)]
    for _ in range(k):
        for j in range(1, n):
            floor[j] += floor[j - 1]
    print(floor[-1])

# 파스칼의 삼각형 - https://ko.wikipedia.org/wiki/%ED%8C%8C%EC%8A%A4%EC%B9%BC%EC%9D%98_%EC%82%BC%EA%B0%81%ED%98%95
# 파스칼의 삼각형의 원리에 따라 바로 아래층과 이전 호수의 인원 수를 합치면 현재 호수의 인원수가 나온다.
# https://ooyoung.tistory.com/89

# import math

# i = input
# for n in [int] * int(i()):
#     k = n(i())
#     print(math.comb(k + n(i()), k + 1))

# math.comb - https://docs.python.org/ko/3/library/math.html#math.comb
