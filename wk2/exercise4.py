# Exercise 4.1
# Are the following two distributions equivalent?

import random


def dist1():
    return random.random() * 2 - 1


def dist2():
    if random.random() > 0.5:
        return random.random()
    else:
        return random.random() - 1


# Testing dist2 to see how often it returns a value less than 0
def test_dist2_negative():
    negative_count = 0
    total_calls = 100000

    for _ in range(total_calls):
        if dist2() < 0:
            negative_count += 1

    percentage = (negative_count / total_calls) * 100
    return percentage


print("Returns percentage times less than 0", test_dist2_negative())

dist1()
dist2()


# Exercise 4.2
# Are the following two distributions equivalent?

import random


def dist3():
    return int(random.random() * 10)


def dist4():
    return random.randrange(0, 10)


dist3()
dist4()
