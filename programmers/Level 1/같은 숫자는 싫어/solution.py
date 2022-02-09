def solution(arr):
    return [e for i, e in enumerate(arr) if not i or (i and arr[i - 1] != e)]


# def solution(arr):
#     for i in range(len(arr) - 1, 0, -1):
#         if arr[i - 1] == arr[i]:
#             del arr[i]
#     return arr

# 위의 코드가 효율성 테스트에서 실패하는 이유
# https://programmers.co.kr/questions/23471
# 배열의 원소를 제거하면 다른 원소들을 앞으로 옮기면서 이동 작업을 수행하기 떄문

# 슬라이싱은 인덱스 값이 범위 초과해도 오류가 발생하지 않고, 그냥 빈 배열이 나온다

# def solution(arr):
#     a = []
#     for i in arr:
#         if a[-1:] == [i]:
#             continue
#         a.append(i)
#     return a


# def solution(arr):
#     return [arr[i] for i in range(len(arr)) if [arr[i]] != arr[i + 1 : i + 2]]
