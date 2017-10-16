from random import normalvariate


def simple_cut(cut_sigma, deck, _):
    cut = round(normalvariate(0.5, cut_sigma) * len(deck))

    shuffled = deck[cut:]
    shuffled.extend(deck[:cut])

    return shuffled