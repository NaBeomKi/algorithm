while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break

# for a, _, b, _ in open(0):
#     print(int(a) + int(b))

# ############################

# try:
#     while 1:
#         print(eval("+".join(input())))
# except:
#     1

# [BOJ] 입출력에서 readline()과 input()의 EOF 입력시 차이점
# https://joewithtech.tistory.com/26

# [입출력] boj 11718, 11719 - EOF 판단
#  https://phin09.tistory.com/18

# ############################

# except 에러 종류를 명시하는게 좋다 - do not use bare 'except'
# 지금 상황에서는 EOFError
