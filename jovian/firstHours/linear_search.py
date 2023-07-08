# Alice has some cards with numbers written on them. She arranges the cards in
# decreasing order, and lays them out face down in a sequence on a table. She challenges
# Bob to pick out the card containing a given number by turning over as few cards as possible.
# Write a function to help Bob locate the card.

from jovian.pythondsa import evaluate_test_cases

tests = []
test = {
    'input': {
        'cards': [],
        'query': 1
    },
    'output': -1
}
tests.append(test)

test = {
    'input': {
        'cards': [23, 12, 2, 1],
        'query': 12
    },
    'output': 1
}
tests.append(test)

test3 = {
    'input': {
        'cards': [-1, -2, -4, -8, -13],
        'query': -8
    },
    'output': 3
}
tests.append(test3)

test = {
    'input': {
        'cards': [9, 8, 6, 6, 6, 4, 4, 2, 2, 1],
        'query': 6
    },
    'output': 2
}
tests.append(test)

test = {
    'input': {
        'cards': [9, 8, 6, 6, 6, 4, 4, 2, 2, 1],
        'query': 3
    },
    'output': -1
}
tests.append(test)


def card_location(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1

    return -1


def repeat_loc(mid, cards, query):
    mid_pos = cards[mid]
    if mid_pos == query:
        if mid < len(cards) and cards[mid-1] == query:
            return 'left'
        else:
            print(mid)
            return 'found'

    if mid_pos > query:
        return 'right'
    elif mid_pos < query:
        return 'left'
    

def card_binary_search(cards, query):
    lo, hi = 0, len(cards) - 1
    while lo <= hi:
        mid = (lo+hi) // 2
        result = repeat_loc(mid, cards, query)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1


# evaluate_test_cases(card_binary_search, tests)
card_binary_search(**test3['input'])
