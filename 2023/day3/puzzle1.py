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


part_nums = []
for num in nums:
    row = num[1]  # num in row
    nsi = num[2]  # num start index
    nei = num[3]  # num end index
    part_num_found = False
    for r in range(row - 1, row + 2):
        if part_num_found:
            break
        for c in range(nsi - 1, nei + 2):
            if part_num_found:
                break
            try:
                if r == row and c in range(nsi, nei + 1):
                    pass
                else:
                    if is_symbol(schema[r][c]):
                        part_nums.append(num[0])
                        part_num_found = True
            except BaseException:
                continue

    # not so nice implementation of above loops below

    # if nsi > 0:  # before number
    #
    #     # same row
    #     char = schema[row][nsi - 1]
    #     if is_symbol(char):
    #         part_nums.append(num[0])
    #         continue
    #
    #     # top-left diagonal
    #     if row > 0:
    #         char = schema[row - 1][nsi - 1]
    #         if is_symbol(char):
    #             part_nums.append(num[0])
    #             continue
    #
    #     # bottom-left diagonal
    #     if row < len(schema) - 1:
    #         char = schema[row + 1][nsi - 1]
    #         if is_symbol(char):
    #             part_nums.append(num[0])
    #             continue
    #
    # if nei < len(schema[0]) - 1:  # after number
    #
    #     # same row
    #     char = schema[row][nei + 1]
    #     if is_symbol(char):
    #         part_nums.append(num[0])
    #         continue
    #
    #     # top-right diagonal
    #     if row > 0:
    #         char = schema[row - 1][nei + 1]
    #         if is_symbol(char):
    #             part_nums.append(num[0])
    #             continue
    #
    #     # bottom-right diagonal
    #     if row < len(schema) - 1:
    #         char = schema[row + 1][nei + 1]
    #         if is_symbol(char):
    #             part_nums.append(num[0])
    #             continue
    #
    # # above and below number
    # for ix in range(nei - nsi + 1):
    #
    #     # above row
    #     if row > 0:
    #         char = schema[row - 1][nsi + ix]
    #         if is_symbol(char):
    #             part_nums.append(num[0])
    #             break
    #
    #     # below row
    #     if row < len(schema) - 1:
    #         char = schema[row + 1][nsi + ix]
    #         if is_symbol(char):
    #             part_nums.append(num[0])
    #             break

print(sum(part_nums))
