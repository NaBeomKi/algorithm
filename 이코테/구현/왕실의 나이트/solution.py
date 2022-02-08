row, column = [i for i in input()]
column = int(ord(column)) - int(ord("a")) + 1
steps = [
    (-2, -1),
    (-1, -2),
    (1, -2),
    (2, -1),
    (2, 1),
    (1, 2),
    (-1, -2),
    (-2, 1),
]
result = 0
for step in steps:
    n_row = row + step[0]
    n_column = column + step[1]
    if n_row >= 1 and n_row <= 8 and n_column >= 1 and n_column <= 8:
        result += 1
print(result)
