from itertools import repeat
from math import lcm

with open("input", "r") as f:
    input = [line.strip() for line in f.readlines()]
    f.close()

test = """\
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)\
"""

# input = test.split("\n")
instructions = input[0].replace("L", "0").replace("R", "1")
maps = {}
for line in input[2:]:
    parts = line[7:-1].partition(", ")
    maps[line[:3]] = (parts[0], parts[-1])

counts = []
for current in filter(lambda x: x.endswith("A"), maps.keys()):
    count = 0
    first_z = None

    while not current.endswith("Z"):
        for ins in instructions:
            current = maps[current][int(ins)]
            count += 1

    counts.append(count)

print(counts)
print(lcm(*counts))
