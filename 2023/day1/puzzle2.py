import re


with open("input", "r") as f:
    input = [line.strip() for line in f.readlines()]
    f.close()

char_nums = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}

test = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


def find_cal_num(line) -> int:
    regex = r"(?=(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))"
    matches = re.finditer(regex, line)
    nums = [match.groups(0)[0] for match in matches]
    return int(char_nums[nums[0]] + char_nums[nums[-1]]
               ) if len(nums) > 0 else 0


# print(sum([find_cal_num(line) for line in test.split("\n")]))
print(sum([find_cal_num(line) for line in input]))
