while n := int(input()):
    bool_list = [True] * (2 * n + 1)
    for i in range(2):
        bool_list[i] = False
    for i in range(2, int((2 * n + 1) ** 0.5) + 1):
        for j in range(i + i, 2 * n + 1, i):
            bool_list[j] = False
    print(len([i for i in range(n + 1, 2 * n + 1) if bool_list[i]]))

# m = 999999
# i, e = 1, [1] * (m + 1)
# while (i := i + 1) * i < m + 1:
#     if e[i]:
#         e[2 * i :: i] = [0] * (m // i - 1)
# while (n := int(input())) > 0:
#     print(sum(e[n + 1 : 2 * n + 1]))
