max_score = max(score_list := [*map(int, [*open(0)][1].split())])
print(sum(score_list) / max_score * 100 / len(score_list))

# n, *l = map(int, open(0).read().split())
# print(sum(l) * 100 / max(l) / n)
