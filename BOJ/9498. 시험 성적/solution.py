score = int(input())
print(
    "A"
    if score >= 90 and score <= 100
    else (
        "B"
        if score >= 80
        else ("C" if score >= 70 else ("D" if score >= 60 else "F"))
    )
)

# print("FFFFFFDCBAA"[int(input()) // 10])
