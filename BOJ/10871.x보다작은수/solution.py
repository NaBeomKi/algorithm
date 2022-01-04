import sys

input = sys.stdin.readline
length, max_num = map(int, input().split())
for i in map(int, input().split()):
    if i < max_num:
        print(i, end=" ")

# n, x, *a = map(int, open(0).read().split())
# for i in a:
#     i < x != print(i)

# python 에서는 (a < b) && (b < c) 를 a < b < c 로 줄일 수 있다.
# 따라서 i < x != print(i) 는 (i < x) && (x != print(i)) 와 동일하다.
# 두번째 조건을 평가할 때, print(i)는 함수 실행문으로 평가 결과와는 상관없이 출력되기 때문에
# != 말고도 비교연산자라면 무엇이 되어도 상관없는 상황
# https://www.acmicpc.net/board/view/80772#comment-131725
