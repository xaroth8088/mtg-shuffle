from random import normalvariate


def riffle(cut_sigma, deck, random):
    shuffled = []

    # First, cut the deck
    cut = round(normalvariate(0.5, cut_sigma) * len(deck))

    deck_a = deck[:cut]
    deck_b = deck[cut:]

    # Until one or both subdecks are empty, pick a card from either subdeck to put into the shuffled deck.
    # The probability for which deck to pull from is relative to the size of each pile.
    while len(deck_a) > 0 and len(deck_b) > 0:
        roll = random()
        if roll < (len(deck_a) / (len(deck_a) + len(deck_b))):
            shuffled.insert(0, deck_a.pop())
        else:
            shuffled.insert(0, deck_b.pop())

    # When either deck is empty, just append the rest of the other one to the shuffled deck
    shuffled = deck_a + shuffled
    shuffled = deck_b + shuffled

    return shuffled
