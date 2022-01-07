for case_list in [*open(0)][1:]:
    total_len, *score_list = map(int, case_list.split())
    aver = sum(score_list) // total_len
    print(
        "{:.3f}%".format(
            sum((n := 1 * (j > aver)) for j in score_list) / total_len * 100
        )
    )

# exec(
#     int(input())
#     * 'b,*c=map(int,input().split());print(f"{sum(b*i>sum(c)for i in c)/b:.3%}");'
# )

# 아래의 코드를 처음 인풋 값만큼 반복하는데,
# b, *c = map(int, input().split())
# print(f"{sum(b * i > sum(c) for i in c) / b:.3%}")

# 50 50 70 80 100 # 학생 수 제외
# 위의 입력값을 받아

# b * i > sum(c) for i in c
# 위 코드를 리스트형으로 변환해 출력하면

# [False, False, False, True, True]
# 위의 값이 출력된다.
