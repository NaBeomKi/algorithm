for i in range(int(input())):
    h, w, n = map(int, input().split())
    print(
        f'{floor if (floor:=n%h) else h}{"0"+str(ho) if (ho:=(n+h-1)//h) < 10 else ho}'
    )

# 문제에서 제시한 예시를 시계 방향으로 90도로 회전한 형태로 보면 문제를 이해하기 수월해진다.
# 즉 아래와 같은 리스트의 형태로 생각해보는 것

# 101 201 301 401 501 ... H01
# 102 202 302 402 502 ... H01
# 103 203 303 403 503 ... H01
# 104 204 304 404 504 ... H01
# ...
# 10W 20W 30W 40W 50W ... HW

# W는 호수의 뒷자리의 최댓값, H는 호수의 앞자리의 최댓값.
# n번째 방은
# 1. n%h 로 몇 번째 층에 속하는지,
# 2. n/h 로 몇 번째 방번호(뒷자리)인지 알 수 있다.
# 주의할 점
# 1. n%h가 나눠떨어지면(0)이면 가장 끝 층.
# 2. n/h는 나눠떨어지지 않으면 소수점이 나올 수 있는데 방번호는 정수이므로 올림 처리

# 주의할 점 - https://www.acmicpc.net/board/view/80101
# 올림 - https://www.acmicpc.net/board/view/79818

# for r in [*open(0)][1:]:
#     h, _, n = map(int, r.split())
#     n -= 1
#     print((n % h + 1) * 100 + n // h + 1)
