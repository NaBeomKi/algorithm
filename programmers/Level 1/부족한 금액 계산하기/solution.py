def solution(price, money, count):
    lack = sum(price * i for i in range(1, count + 1)) - money
    return 0 if lack < 0 else lack


# 등차수열의 합 공식 그리고 max

# def solution(price, money, count):
#     return max(0, price * (count + 1) * count // 2 - money)
