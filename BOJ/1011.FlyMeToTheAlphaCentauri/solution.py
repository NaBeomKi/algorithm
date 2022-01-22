for _ in range(int(input())):
    x, y = map(int, input().split())
    distance = abs(x - y)
    max_len = int(distance ** 0.5)
    if max_len == distance ** 0.5:
        print(2 * max_len - 1)
    elif distance <= max_len * max_len + max_len:
        print(2 * max_len)
    else:
        print(2 * max_len + 1)

# [백준] 1011번 : Fly me to the Alpha Centauri - JAVA [자바] - https://st-lab.tistory.com/79
# 직접 세본 것 - https://docs.google.com/spreadsheets/d/1jOV_5nfmsqfKZOoFvC3AE6H8uYH6lW_vuP3uFQbSUNQ/edit#gid=0
# [C 언어] 백준 1011. Fly me to the Alpha Centauri - https://mjeong9316.tistory.com/147

# for i in [int] * int(input()):
#     x, y = input().split()
#     print(i(2 * (i(y) - i(x) - 0.5) ** 0.5))
