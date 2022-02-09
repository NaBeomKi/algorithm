def solution(arr, divisor):
    result = sorted([i for i in arr if not i % divisor])
    return result if result else [-1]


# def solution(arr, divisor):
#     return sorted([n for n in arr if n % divisor == 0]) or [-1]
