def solution(s, n):
    answer = ""
    alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 2
    alpha_lower = "abcdefghijklmnopqrstuvwxyz" * 2
    for i in s:
        if i in alpha_upper:
            answer += alpha_upper[alpha_upper.find(i) + n]
        elif i in alpha_lower:
            answer += alpha_lower[alpha_lower.find(i) + n]
        else:
            answer += i
    return answer


# 좋은 다른 풀이들이 너무 많아서 링크로 대체
# https://programmers.co.kr/learn/courses/30/lessons/12926/solution_groups?language=python3
