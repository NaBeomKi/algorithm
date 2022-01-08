not_self_list = set()
for i in (num_list := {*range(1, 10001)}):
    not_self_list.add(i + sum(int(j) for j in str(i)))
print(*sorted(num_list - not_self_list), sep="\n")

# set 두 개를 만들어 셀프넘버가 아닌 숫자들을 모은 뒤, 차집합을 구한다. https://wook-2124.tistory.com/252

# r = range(9999)
# print(*sorted({*r} - {n + sum(map(int, str(n))) for n in r}))
