print(
    max_num := max(num_list := [*map(int, open(0).read().split())]),
    num_list.index(max_num) + 1,
    sep="\n",
)

# max_num = 0
# max_num_index = 0
# for i in range(9):
#     current_num = int(input())
#     if max_num < current_num:
#         max_num = current_num
#         max_num_index = i + 1
# print(max_num, max_num_index)

# 위는 내 또 다른 답. index+1 해야한다는걸 나중에 알아서 한참을 헤맸다.

# print(*max((int(input()), i + 1) for i in range(9)))

# 반복문을 돌며 입력된 숫자와 인덱스를 튜플로 묶는다.
# 이 후 모든 튜플을 max함수에 넣어 비교를 진행한다. (각각의 요소를 비교하게 된다.)
# 하나의 튜플이 반환되면, 그 첫번째 요소로 접근한다. 따라서 문제에서 원하는 결과값이 출력된다.
