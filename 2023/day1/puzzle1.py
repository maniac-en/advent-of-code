import re


with open("input", "r") as f:
    input = [line.strip() for line in f.readlines()]
    f.close()


test = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""


def find_cal_num(line) -> int:
    regex = r"(?=(1|2|3|4|5|6|7|8|9))"
    matches = re.finditer(regex, line)
    nums = [match.groups(0)[0] for match in matches]
    return int(nums[0] + nums[-1]) if len(nums) > 0 else 0


# print(sum([find_cal_num(line) for line in test.split("\n")]))
print(sum([find_cal_num(line) for line in input]))
