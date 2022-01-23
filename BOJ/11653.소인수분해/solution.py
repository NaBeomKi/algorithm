n = int(input())
for i in range(2, int(n ** (1 / 2)) + 1):
    if n == 1:
        break
    while not n % i:
        print(i)
        n //= i
if not n == 1:
    print(n)

# N = int(input())
# a = 2
# while N > 1:
#     if N % a:
#         a += 1
#     else:
#         print(a)
#         N /= a
