n, m, k = map(int, input().split())
data = [*map(int, input().split())]
data.sort()
max_num, sec_max_num = data[-1], data[-2]

result = 0
if max_num == sec_max_num:
    result = max_num * m
else:
    result = ((max_num * k + sec_max_num) * (m // (k + 1))) + (
        (m % (k + 1)) * max_num
    )
print(result)

# # N, M, K를 공백을 기준으로 구분하여 입력 받기
# n, m, k = map(int, input().split())
# # N개의 수를 공백을 기준으로 구분하여 입력 받기
# data = list(map(int, input().split()))

# data.sort()  # 입력 받은 수들 정렬하기
# first = data[n - 1]  # 가장 큰 수
# second = data[n - 2]  # 두 번째로 큰 수

# # 가장 큰 수가 더해지는 횟수 계산
# # 수열이 반복되는 횟수 m/(k+1), 여기에 다시 k를 곱해주면 가장 큰 수가 등장하는 횟수
# # m/(k+1)가 나누어 떨어지지 않을 경우, 나머지만큼 가장 큰수가 더해짐.
# count = int(m / (k + 1)) * k
# count += m % (k + 1)

# result = 0
# result += (count) * first  # 가장 큰 수 더하기
# result += (m - count) * second  # 두 번째로 큰 수 더하기

# print(result)  # 최종 답안 출력
