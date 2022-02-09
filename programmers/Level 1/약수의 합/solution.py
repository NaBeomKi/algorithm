def solution(n):
    return sum(i for i in range(1, n + 1) if not n % i)


# 자기 자신을 제외한 모든 약수 중 가장 큰 수는 절반을 넘지 못한다.
# 위 방법을 제곱근으로 하게 되면 포함되지 못하는 약수들이 존재함
# ex) 12 -> 모든 약수: [1,2,3,4,6,12], 제곱근 : 3.xx
# 제곱근으로 계산하기 위해선 다른 처리를 해주어야함

# def solution(n):
#     return n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0])
