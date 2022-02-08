def solution(num):
    count = 0
    while num > 1:
        if count > 500:
            break
        if num % 2:
            num = num * 3 + 1
        else:
            num /= 2
        count += 1
    return -1 if count > 500 else count


# 위를 개선

# def solution(num):
#     count = 0
#     while num > 1:
#         if count > 500:
#             return -1
#         if num % 2:
#             num = num * 3 + 1
#         else:
#             num /= 2
#         count += 1
#     return count

# 아래는 다른 풀이

# def solution(num):
#     if num == 1:
#         return 0
#     for i in range(500):
#         num = num / 2 if num % 2 == 0 else num * 3 + 1
#         if num == 1:
#             return i + 1
#     return -1
