from pathlib import Path

from aoc.day3 import solve_1, solve_2, solve
import pytest
from tests.aoc_utils import load_data


@pytest.fixture()
def example_data():
    data = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
    return data.splitlines()


@pytest.fixture()
def input_data():
    return load_data(Path(__file__).parent / 'data' / 'day3_data')


def test_part1_example(example_data):
    assert solve_1(example_data) == 7


def test_part2_example(example_data):
    """
    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
    In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively;
    multiplied together, these produce the answer 336.
    """
    map = example_data
    assert solve(map, delta_x=1) == 2
    assert solve(map, delta_x=3) == 7
    assert solve(map, delta_x=5) == 3
    assert solve(map, delta_x=7) == 4
    assert solve(map, delta_x=1, delta_y=2) == 2
    assert solve_2(map) == 336


def test_part1(input_data):
    assert solve_1(input_data) == 280


def test_part2(input_data):
    assert solve_2(input_data) == 4355551200
