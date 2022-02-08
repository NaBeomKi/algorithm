len = int(input())
for i in range(1, len + 1):
    print(" " * (len - i) + "*" * i)

# i, n = 0, int(input())
# while n - i:
#     i += 1
#     print(f'{"*"*i:>{n}}')
