with open("input", "r") as f:
    input = [line.strip() for line in f.readlines()]
    f.close()

test = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

# has an edge case of 633 on 3rd row
test2 = """
467..114..
...*......
..35...633
.......#..
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

# schema = [[ch for ch in line] for line in test.split("\n")[1:-1]]
schema = [[ch for ch in line] for line in input]

nums = []
num_start = None

for rx, r in enumerate(schema):  # row index, row
    num_not_found = True
    for cx, c in enumerate(r):  # column index, col
        if c.isdigit():
            if num_not_found:
                num_not_found = False
                num_start = cx
        elif not num_not_found:
            nums.append(
                (int("".join(r[num_start:cx])), rx, num_start, cx - 1))
            num_start = None
            num_not_found = True
    if not num_not_found:
        nums.append((int("".join(r[num_start:cx + 1])), rx, num_start, cx))


def is_symbol(char) -> bool:
    return (not char.isdigit() and char != ".")


def is_part_num(num) -> bool:
    row = num[1]  # num in row
    nsi = num[2]  # num start index
    nei = num[3]  # num end index

    for r in range(row - 1, row + 2):
        for c in range(nsi - 1, nei + 2):
            try:
                if r == row and c in range(nsi, nei + 1):
                    pass
                else:
                    if is_symbol(schema[r][c]):
                        return True
            except BaseException:
                continue

    return False


def get_num(row, col) -> int:
    for num in filter(lambda num: num[1] == row, nums):
        if col >= num[2] and col <= num[3]:
            return num


def show_neighbours(r, c):
    s = ""
    for i in range(-1, 2):
        for j in range(-1, 2):
            try:
                s += f" {schema[r+i][c+j]}"
            except BaseException:
                s += " !"
                continue
        s += "\n"
    return s


gear_ratios = []
for rx, r in enumerate(schema):  # row index, row
    for cx, c in enumerate(r):  # column index, col
        if c == "*":
            # print(show_neighbours(rx, cx))
            first_part_num = None
            ratio_found = False

            try:
                for a in range(-1, 2):
                    for b in range(-1, 2):
                        if schema[rx + a][cx + b].isdigit():
                            if first_part_num is None:
                                first_part_num = get_num(rx + a, cx + b)
                            else:
                                second_part_num = get_num(rx + a, cx + b)
                                if second_part_num[0] == first_part_num[0] and\
                                        second_part_num[1] == first_part_num[1] and\
                                        second_part_num[2] == first_part_num[2] and\
                                        second_part_num[3] == first_part_num[3]:
                                    continue

                                gear_ratios.append(
                                    first_part_num[0] * second_part_num[0])
                                ratio_found = True
                        if ratio_found:
                            break
                    if ratio_found:
                        break
            except BaseException:
                continue

print(sum(gear_ratios))
