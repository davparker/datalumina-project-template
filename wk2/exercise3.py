# Exercise 3-1

import random


def deterministicNumber():
    """
    Deterministically generates and returns an even number between 9 and 21
    """
    random.seed(10)
    return random.randrange(10, 22, 2)


# Exercise 3-2

import random


def stochasticNumber():
    """
    Stochastically generates and returns an even number between 9 and 21
    """
    # random.seed(10)
    return random.randrange(10, 22, 2)
