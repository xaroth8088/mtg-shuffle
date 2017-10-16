def make_land_spells_deck(num_land, num_spells):
    deck = ["L"] * num_land
    deck.extend(["S"] * num_spells)
    return deck


def make_sequence_deck(deck_size):
    deck = list(range(0, deck_size))
    return deck
