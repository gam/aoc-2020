from itertools import combinations
from math import prod


def solve_1(data):
    return solve(data, tuple_size=2)


def solve_2(data):
    return solve(data, tuple_size=3)


def solve(numbers, tuple_size):
    for candidate in combinations(numbers, tuple_size):
        if sum(candidate) == 2020:
            return prod(candidate)
