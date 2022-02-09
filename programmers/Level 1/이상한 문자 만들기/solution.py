def solution(s):
    return " ".join(
        map(
            lambda x: "".join(
                a.lower() if i % 2 else a.upper() for i, a in enumerate(x)
            ),
            s.split(" "),
        )
    )
    # return " ".join(
    #     map(
    #         lambda x: "".join(
    #             x[i].lower() if i % 2 else x[i].upper() for i in range(len(x))
    #         ),
    #         s.split(" "),
    #     )
    # )


# enumerate
# https://www.daleseo.com/python-enumerate/

# 주의할 점
# 문제의 조건 - 각 단어는 하나 이상의 공백문자로 구분되어 있습니다.
# split(): 여러 개의 공백도 하나로 보고 처리
# split(' '): 각각의 공백을 별도로 처리
# https://somjang.tistory.com/entry/Python-%EB%AC%B8%EC%9E%90%EC%97%B4-split-%EA%B3%BC-split-%EC%B0%A8%EC%9D%B4-%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0
