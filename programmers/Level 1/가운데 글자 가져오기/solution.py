def solution(s):
    mid = len(s) // 2
    return s[mid] if len(s) % 2 else s[mid - 1 : mid + 1]


# def solution(s):
#     return s[(len(s) - 1) // 2 : len(s) // 2 + 1]

# def solution(s):
#   a = len(s)
#     if a % 2 == 0 :
#         a = (a-2) / 2
#     else :
#         a = (a-1) / 2
#     return s[int(a) : -int(a)]
