def interleave(deck, _):
    half = round(len(deck) / 2)
    deck_a = deck[0:half]
    deck_b = deck[half:]
    return [x for t in zip(deck_a, deck_b) for x in t]
