with open("input", "r") as f:
    input = [line.strip() for line in f.readlines()]
    f.close()

test = """Time:      7  15   30
Distance:  9  40  200"""

# input = test.split("\n")
races = [(
    int("".join([i for i in input[0][11:] if i.isdigit()])),
    int("".join([i for i in input[1][11:] if i.isdigit()]))
)]

print(sum(list(map(lambda x: list(
    map(lambda y: y * (x[0] - y) > x[1], range(1, x[0]))).count(True),
    races))))
