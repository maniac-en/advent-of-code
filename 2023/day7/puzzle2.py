from pprint import pprint
from collections import Counter
import sys

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
card_ranks = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']


def get_rank_for_hand(hand) -> list(hand_ranks):
    c = Counter(hand)
    jc = c['J']

    if jc:
        if jc == 4 or jc == 5:
            return [hand_ranks.index('five-of-a-kind')]

        # by this point, jc has to be lesser than 3
        for i, v in c.items():
            if i != 'J' and v + jc == 5:
                return [hand_ranks.index('five-of-a-kind')]

        for i, v in c.items():
            if i != 'J' and v + jc == 4:
                return [hand_ranks.index('four-of-a-kind')]
    else:
        if hand.count(hand[0]) == 5:
            return [hand_ranks.index('five-of-a-kind')]

        elif hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4:
            return [hand_ranks.index('four-of-a-kind')]

    matches = []

    if jc != 0:
        # max count as well as max precedence
        max_repeated_card = max(c, key=lambda x: (c[x], card_ranks.index(x)))
        max_card = max(hand, key=lambda x: card_ranks.index(x))
        if max_repeated_card == 'J':
            matches.append(max_card * (jc + 1))
        else:
            if c[max_repeated_card] + jc == 3:
                matches.append(max_repeated_card * 3)
            elif c[max_repeated_card] + jc == 2:
                matches.append(max_repeated_card * 2)

        for i, v in c.items():
            if i != 'J' and i != max_repeated_card and v > 1:
                matches.append(i * v)
    else:
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
            return [hand_ranks.index('full-house')]
        elif len(matches[0]) == 2 and len(matches[1]) == 2:
            return [hand_ranks.index('two-pair')]

    elif len(matches) == 1:
        if len(matches[0]) == 3:
            return [hand_ranks.index('three-of-a-kind')]
        elif len(matches[0]) == 2:
            return [hand_ranks.index('one-pair')]

    return [hand_ranks.index('high-card')]


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
# print(hand_ranks[get_rank_for_hand('699J6')[0]])
