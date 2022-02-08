def solution(n):
    return int("".join(sorted([i for i in str(n)], reverse=True)))


# sorted하면 리스트로 반환해서 나온다

# def solution(n):
#     return int("".join(sorted(str(n), reverse=True)))
