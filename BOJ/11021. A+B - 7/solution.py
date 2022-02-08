import sys

input = sys.stdin.readline
for i in range(1, int(input()) + 1):
    a, b = map(int, input().split())
    print(f"Case #{i}: {a+b}")

# i = 0
# for a, _, c, _ in [*open(0)][1:]:
#     i += 1
#     print(f"Case #{i}:", int(a) + int(c))
