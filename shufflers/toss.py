from random import normalvariate


def toss(target_fraction, cut_sigma, deck, _):
    shuffled = []

    deck_size = len(deck)

    # While there's still > target_fraction of the deck left...
    while len(deck) > target_fraction * deck_size:
        # Take approximately target_fraction (of the original deck size) cards off the top and put onto the bottom of the
        # shuffled deck, in order
        cut = round(normalvariate(target_fraction, cut_sigma) * deck_size)

        shuffled = deck[:cut] + shuffled
        deck = deck[cut:]

    # Put the rest of the pile onto the shuffled deck
    shuffled.extend(deck)

    return shuffled
