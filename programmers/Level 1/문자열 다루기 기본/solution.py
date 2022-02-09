def solution(s):
    if len(s) in (4, 6):
        return s.isdigit()
    return False


# def solution(s):
#     return s.isdigit() and len(s) in (4, 6)


# def solution(s):
#     try:
#         int(s)
#     except:
#         return False
#     return len(s) == 4 or len(s) == 6


# def solution(s):
#     import re

#     return bool(re.match("^(\d{4}|\d{6})$", s))
