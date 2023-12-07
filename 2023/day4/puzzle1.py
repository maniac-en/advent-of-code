with open("input", "r") as f:
    input = [line.strip() for line in f.readlines()]
    f.close()

test = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

# input = test.split("\n")
total = 0

for card in input:
    count = None
    card_string_split = [e for e in filter(lambda x: x != "", card.split(" "))]
    card_split_ix = card_string_split.index("|")
    winning_numbers = [int(n) for n in card_string_split[2:card_split_ix]]
    lottery_numbers = [int(n) for n in card_string_split[card_split_ix + 1:]]

    for num in lottery_numbers:
        if num in winning_numbers:
            count = count + 1 if count is not None else 1

    if count is not None:
        total += 2 ** (count - 1)

print(total)
