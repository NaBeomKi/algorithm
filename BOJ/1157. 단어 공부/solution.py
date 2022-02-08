word = input().upper()
char_list = [*{i for i in word}]
num_list = [*map(lambda x: word.count(x), char_list)]
print(
    "?"
    if num_list.count(target := max(num_list)) > 1
    else char_list[num_list.index(target)]
)

# 1. 입력된 문자열을 모두 대문자로 변환.
# 2. 각 알파벳의 set을 만들어 중복을 제거하고, 리스트로 변환
# 3. char_list의 각 알파벳을 돌며 문자열에 몇 번 있는지 센 값을 list에 저장
# 4. num_list의 최댓값을 알아내, 몇 해당 리스트에 몇 개가 있는지 확인.
# 5. 1개 보다 많으면 "?", 아니라면 최댓값이 num_list의 몇 번째 인덱스인지 알아낸 후, char_list에서 해당 인덱스의 값을 출력
# https://ooyoung.tistory.com/70

# from statistics import *

# try:
#     t = mode(input().upper())
# except:
#     t = "?"
# print(t)

# statistics - https://docs.python.org/ko/dev/library/statistics.html
# mode: 최빈 값을 찾는 함수 - https://docs.python.org/ko/dev/library/statistics.html#statistics.mode
