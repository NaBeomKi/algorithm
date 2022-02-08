a = int(input())
b = input()
for n in b[::-1]:
    print(a * int(n))
print(a * int(b))

# a, b = map(int, open(0))
# print(b % 10 * a, (b % 100 // 10) * a, (b // 100) * a, b * a)

# open(0)
# https://www.acmicpc.net/board/view/59815
# https://www.acmicpc.net/board/view/54482
# https://docs.python.org/ko/3/library/functions.html?highlight=open#open
# https://stackoverflow.com/questions/53898231/integer-file-descriptor-0-in-open

# 표준입력
# https://shoark7.github.io/programming/knowledge/what-is-standard-stream
# https://ttend.tistory.com/732
# https://www.lesstif.com/lpt/stdin-stdout-stderr-113346293.html
# https://m.blog.naver.com/tipsware/220980651156

# EOF 입력
# https://zetawiki.com/wiki/C%EC%96%B8%EC%96%B4_stdin%EC%97%90_EOF_%EC%9E%85%EB%A0%A5


# //: 나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분의 수만 구함
