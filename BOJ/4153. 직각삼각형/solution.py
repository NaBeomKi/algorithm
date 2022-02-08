while True:
    a, b, c = sorted(map(int, input().split()))
    if not a and not b and not c:
        break
    if a ** 2 + b ** 2 == c ** 2:
        print("right")
    else:
        print("wrong")

# for i in open(0):
#     a, b, c = sorted(map(int, i.split()))
#     print("wrriognhgt"[a * a + b * b == c * c : a * b : 2])
