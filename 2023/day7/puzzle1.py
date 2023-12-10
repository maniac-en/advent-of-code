from pprint import pprint

with open("input", "r") as f:
    input = [line.strip() for line in f.readlines()]
    f.close()

test = """\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483\
"""

# input = test.split("\n")

hand_ranks = [
    'high-card',
    'one-pair',
    'two-pair',
    'three-of-a-kind',
    'full-house',
    'four-of-a-kind',
    'five-of-a-kind']
card_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


def get_rank_for_hand(hand) -> list(hand_ranks):
    ranks = []

    if hand.count(hand[0]) == 5:
        ranks.append(hand_ranks.index('five-of-a-kind'))

    elif hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4:
        ranks.append(hand_ranks.index('four-of-a-kind'))

    matches = []

    for ix, card in enumerate(hand):
        if hand.count(card) == 3:
            if card * 3 not in matches:
                matches.append(card * 3)
        elif hand.count(card) == 2:
            if card * 2 not in matches:
                matches.append(card * 2)

    if len(matches) == 2:
        if (len(matches[0]) == 3 and len(matches[1]) == 2)\
                or (len(matches[1]) == 3 and len(matches[0]) == 2):
            ranks.append(hand_ranks.index('full-house'))
        elif len(matches[0]) == 2 and len(matches[1]) == 2:
            ranks.append(hand_ranks.index('two-pair'))

    elif len(matches) == 1:
        if len(matches[0]) == 3:
            ranks.append(hand_ranks.index('three-of-a-kind'))
        elif len(matches[0]) == 2:
            ranks.append(hand_ranks.index('one-pair'))

    if len(ranks) == 0:
        ranks.append(hand_ranks.index('high-card'))
    return ranks


all_hand_ranks = []
for line in input:
    all_hand_ranks.append((line[:5],
                           get_rank_for_hand(line[:5]),
                           int(line[6:])))


def card_rank_keys(hand):
    return card_ranks.index(hand[0]), \
        card_ranks.index(hand[1]), \
        card_ranks.index(hand[2]), \
        card_ranks.index(hand[3]), \
        card_ranks.index(hand[4])


final = all_hand_ranks
final.sort(key=lambda x: (x[1][0], *card_rank_keys(x[0])))
pprint([(h[0], [hand_ranks[v] for v in h[1]]) for h in final])
print(sum(map(lambda i_v: i_v[1][2] * i_v[0], enumerate(final, start=1))))
