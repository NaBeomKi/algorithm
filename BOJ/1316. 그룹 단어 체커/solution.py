n = count = int(input())
for _ in range(n):
    string = input()
    for i in range(len(string) - 1):
        if string.find(string[i]) > string.find(string[i + 1]):
            count -= 1
            break
print(count)

# 다음 문자가 이전 문자보다 앞선 인덱스에서 발견되면, 그룹 단어가 아니다.
# https://docs.python.org/ko/3/library/stdtypes.html#str.find
# https://docs.python.org/ko/3/library/stdtypes.html#bytes.index

# print(sum([*x] == sorted(x, key=x.find) for x in open(0)) - 1)

# 각각의 글자를 모두 분리해 리스크로 만든 후. 발견한 순서대로 정렬한 것과 비교해 일치하지 않으면 -1
