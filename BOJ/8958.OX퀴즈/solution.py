for line in open(0).read().split()[1:]:
    print(sum(map(lambda x: (n := len(x)) * (n + 1) // 2, line.split("X"))))

# for i in [*open(0)][1:]:
#     n = 0
#     print(sum((n := (n + 1) * (j == "O")) for j in i))

# X가 들어오는 순간 n이 0이 되면서 초기화
