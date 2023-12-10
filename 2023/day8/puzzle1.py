from itertools import repeat
import sys

with open("input", "r") as f:
    input = [line.strip() for line in f.readlines()]
    f.close()

test = """\
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)\
"""

test = """\
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)\
"""

# input = test.split("\n")

instructions = input[0].replace("L", "0").replace("R", "1")
maps = {}
for line in input[2:]:
    parts = line[7:-1].partition(", ")
    maps[line[:3]] = (parts[0], parts[-1])

current = 'AAA'
count = 0
while current != 'ZZZ':
    for ins in instructions:
        if current == 'ZZZ':
            break
        current = maps[current][int(ins)]
        count += 1

print(count)
