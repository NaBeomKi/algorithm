def solution(s):
    nums = [*map(int, s.split())]
    return f"{min(nums)} {max(nums)}"
