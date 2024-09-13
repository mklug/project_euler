# Poker hands.
from collections import Counter

card_ranks = '23456789TJQKA'

def ordered(hand):
    return sorted([card_ranks.index(card[0]) for card in hand],
                  key=lambda x : -x)

def frequency_ordered(hand):
    vals = [card[0] for card in hand]
    count = Counter(vals)
    vals = list(set(vals))
    vals.sort(key=lambda val: (-count[val], -card_ranks.index(val)))
    return [card_ranks.index(val) for val in vals]

def default(hand):
    return (True, ordered(hand))

def one_pair(hand):
    values = set([card[0] for card in hand])
    suits  = set([card[1] for card in hand])
    return (len(values) == 4 and len(suits) > 1,
            frequency_ordered(hand))

def two_pairs(hand):
    value_count = Counter()
    for card in hand:
        value_count[card[0]] += 1
    pairs = 0
    for v in value_count.values():
        if v == 2:
            pairs += 1
    return (pairs == 2,
            frequency_ordered(hand))

def three_of_a_kind(hand):
    value_count = Counter()
    for card in hand:
        value_count[card[0]] += 1
    three = 0
    pairs = 0
    for v in value_count.values():
        if v == 2:
            pairs += 1
        elif v == 3:
            three += 1
    return (pairs == 0 and three == 1,
            frequency_ordered(hand))

def straight(hand):
    ranks = set([card_ranks.index(card[0])
                  for card in hand])
    max_dist = 0
    for i in ranks:
        for j in ranks:
            max_dist = max(max_dist, abs(i-j))
    return (len(ranks) == 5 and max_dist == 4,
            ordered(hand))

def flush(hand):
    suits  = set([card[1] for card in hand])
    return (len(suits) == 1,
            ordered(hand))

def full_house(hand):
    value_count = Counter()
    for card in hand:
        value_count[card[0]] += 1
    three = 0
    pairs = 0
    for v in value_count.values():
        if v == 2:
            pairs += 1
        elif v == 3:
            three += 1
    return (pairs == 1 and three == 1,
            frequency_ordered(hand))

def four_of_a_kind(hand):
    value_count = Counter()
    for card in hand:
        value_count[card[0]] += 1
    four = 0
    for v in value_count.values():
        if v == 4:
            four += 1
    return (four == 1,
            frequency_ordered(hand))

def straight_flush(hand):
    return (straight(hand)[0] and flush(hand)[0],
            ordered(hand))


possibilities = [default,
                 one_pair,
                 two_pairs,
                 three_of_a_kind,
                 straight,
                 flush,
                 full_house,
                 four_of_a_kind,
                 straight_flush]
def rank(hand):
    highest_index = 0
    for i,f in enumerate(possibilities):
        if f(hand)[0]:
            highest_index = i
    return (highest_index, 
            possibilities[highest_index](hand)[1])

if __name__ == '__main__':

    p1_hands = []
    p2_hands = []

    with open('54_poker.txt') as f:
        for line in f:
            line = line.strip().split(' ')
            p1_hands.append(line[:5])
            p2_hands.append(line[5:])

    res = 0
    for p1_hand, p2_hand in zip(p1_hands, p2_hands):
        if rank(p1_hand) > rank(p2_hand):
            res += 1

    print(f'answer = {res}')