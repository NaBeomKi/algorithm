m, n = int(input()), int(input())
num_set = set(range(m, n + 1))
not_prime_set = set()
for i in num_set:
    if i <= 1:
        not_prime_set.add(i)
        continue
    for j in range(2, int(i ** (1 / 2)) + 1):
        if not i % j:
            not_prime_set.add(i)
            break
prime_set = num_set - not_prime_set
if not len(prime_set):
    print(-1)
else:
    print(sum(prime_set))
    print(min(prime_set))

# r = range
# n, m = map(int, open(0))
# print(
#     *[sum(l), l[0]]
#     if (l := [i for i in r(max(2, n), m + 1) if all(i % j for j in r(2, i))])
#     else [-1]
# )

# 비어있는 list, set은 boolean으로 형변환하면 False가 된다.
# 하지만 False와 직접 비교시에는 일치하지 않음 - [] == False => False
# 모든 iterable 객체가 이와 같은지는 아직 모르겠음
