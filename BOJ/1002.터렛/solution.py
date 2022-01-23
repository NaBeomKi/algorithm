for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    sum_r = r1 + r2
    subt_r = abs(r1 - r2)
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if not distance and r1 == r2:
        print(-1)
    elif subt_r < distance < sum_r:
        print(2)
    elif sum_r == distance or subt_r == distance:
        print(1)
    elif sum_r < distance or subt_r > distance:
        print(0)

# ★☆★☆★ 터렛 FAQ ★☆★☆★
# https://www.acmicpc.net/board/view/38854

# 백준저지 1002번 터렛 문제 풀이
# https://eine.tistory.com/entry/%EB%B0%B1%EC%A4%80%EC%A0%80%EC%A7%80-1002%EB%B2%88-%ED%84%B0%EB%A0%9B-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4

# 두 점 사이의 거리, 좌표평면위의 두 점 사이의 거리
# https://mathbang.net/408

# 반례 - https://www.acmicpc.net/board/view/81251

# exec(
#     "x,y,r,X,Y,R=map(int,input().split());a=(X-x)**2+(Y-y)**2;b=(R+r)**2;c=(R-r)**2;print([[1+(a!=b)*(a!=c),-1][a+c<1],0][a>b or a<c]);"
#     * int(input())
# )

# for T in range(int(input())):
#     x1, y1, r1, x2, y2, r2 = map(int, input().split())
#     dsq = (x1 - x2) ** 2 + (y1 - y2) ** 2
#     # d = 0
#     if dsq == 0:
#         print(0 if r1 != r2 else -1)
#         continue
#     # r1+r2 = d or |r1-r2| = d
#     if (r1 + r2) ** 2 == dsq or (r1 - r2) ** 2 == dsq:
#         print(1)
#         continue
#     # r1+r2 < d or |r1-r2| > d
#     if (r1 + r2) ** 2 < dsq or (r1 - r2) ** 2 > dsq:
#         print(0)
#         continue
#     # else
#     print(2)
