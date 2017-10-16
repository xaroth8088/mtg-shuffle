from functools import partial
import configparser

from shufflers.interleave import interleave
from shufflers.riffle import riffle
from shufflers.toss import toss
from shufflers.simple_cut import simple_cut

config = configparser.ConfigParser()
config.read(['config.ini'])


# To construct a shuffling strategy, create partials for each desired shuffler w/configuration, and append to the list
def configure_shuffler():
    cut_sigma = config.getfloat("riffle", "cut_sigma")

    # shufflers = [interleave]
    shufflers = []

    shufflers.extend(
        [
            partial(riffle, cut_sigma),
        ] * 4
    )

    shufflers.extend(
        [
            partial(simple_cut, cut_sigma),
            partial(riffle, cut_sigma),
        ] * 2
    )

    # shufflers.extend(
    #     [
    #         partial(riffle, cut_sigma),
    #         partial(simple_cut, cut_sigma)
    #         # partial(toss, 1/6, cut_sigma),
    #     ] * 3
    # )
    # shufflers.extend([partial(riffle, cut_sigma)] * 6)

    return shufflers
