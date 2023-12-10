from itertools import pairwise
from functools import reduce

with open("input", "r") as f:
    input = [line.strip() for line in f.readlines()]
    f.close()

test = """\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45\
"""

# input = test.split("\n")

histories = [[int(n) for n in line.split()] for line in input]

sum = 0

for history in histories:
    ev = 0  # extrapolated_value
    # print(f"\n{history}")
    diffs = [b - a for a, b in pairwise(history)]
    history_starts = []
    while not all(map(lambda x: x == 0, diffs)):
        history_starts.append(diffs[0])
        diffs = [b - a for a, b in pairwise(diffs)]

    for ix in range(len(history_starts) - 1, -1, -1):
        ev = history_starts[ix] - ev
    sum += history[0] - ev
    history.insert(0, history[0] - ev)
    # print(f"\n{history}")
print(sum)
