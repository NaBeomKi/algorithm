n, k = map(int, input().split())
i = 0
while n != 1:
    i += 1
    if not n % k:
        n //= k
        continue
    n -= 1
print(i)

# 문제의 조건에 따라 위 코드도 맞지만,
# 아래의 코드가 시간복잡도가 더 낮기 때문에 입력된 수가 커지면 커질 수록 더 빠르게 실행된다.

# n, k = map(int, input().split())
# result = 0
# while True:
#     # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
#     # ex) 25/3=8.33333..., 25//3=8 즉 다시 k를 곱하면 k로 나눌 수 있는 수가 됨
#     target = (n // k) * k
#     result += n - target
#     n = target
#     # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 탈출
#     if n < k:
#         break
#     # K로 나누기
#     result += 1
#     n //= k

# # 마지막으로 남은 수에 대하여 1씩 빼기
# result += n - 1
# print(result)
