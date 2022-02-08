count = input()
num_list = list(map(int, input().split()))
min_num = max_num = num_list[0]

for i in num_list:
    if i < min_num:
        min_num = i
        continue
    if i > max_num:
        max_num = i
        continue

print(min_num, max_num)

# print(min(a := [*map(int, [*open(0)][1].split())]), max(a))

# [*open(0)] -> ['5\n', '20 10 35 30 7\n']
# open이 파일 객체를 반환하는데, 개행으로 구분되는 이터러블 객체
# 따라서 map(int,[*open(0)][1:].split()) -> ['20 10 35 30 7\n'].split() 형태가 되기 때문에 오류가 발생

# [*open(0)][1:][0].split() -> ['20', '10', '35', '30', '7']

# or

# [*open(0)][1].split() -> ['20', '10', '35', '30', '7']

# or

# open(0).read() # '5\n 20 10 35 30 7\n' -> 통째로 하나의 문자열
