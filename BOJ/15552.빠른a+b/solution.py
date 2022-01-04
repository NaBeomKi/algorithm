import sys

input = sys.stdin.readline
len = int(input())
for _ in range(len):
    a, b = map(int, input().split())
    print(a + b)

# for l in [*open(0)][1:]:
#     print(sum(map(int, l.split())))
