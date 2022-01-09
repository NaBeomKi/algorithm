for i in range(int(input())):
    count, string = input().split()
    print("".join(j * int(count) for j in string))

# for r, _, *s, _ in [*open(0)][1:]:
#     print("".join(c * int(r) for c in s))
