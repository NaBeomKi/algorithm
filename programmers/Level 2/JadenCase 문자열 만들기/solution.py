def solution(s):
    return " ".join(
        i if i == "" else i[0].upper() + i[1:].lower() for i in s.split(" ")
    )


# 참고하면 좋을 내장함수
# title - https://zetawiki.com/wiki/%ED%8C%8C%EC%9D%B4%EC%8D%AC_title()
# capitalize - https://zetawiki.com/wiki/%ED%8C%8C%EC%9D%B4%EC%8D%AC_%EB%AC%B8%EC%9E%90%EC%97%B4_capitalize()
