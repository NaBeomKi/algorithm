def solution(s):
    count = 0
    for i in s:
        if count < 0:
            return False
        if i == "(":
            count += 1
        else:
            count -= 1
    return count == 0
