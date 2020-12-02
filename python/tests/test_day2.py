from pathlib import Path

import aoc.day2 as day2
import pytest
from aoc.aoc_utils import load_data

EXAMPLE_DATA = ["1-3 a: abcde",
                "1-3 b: cdefg",
                "2-9 c: ccccccccc"]
DATA_DIR = Path(__file__).parent / 'data'


@pytest.fixture()
def input_data():
    return load_data(DATA_DIR / 'day2_data')


def test_day2_part1_example():
    assert day2.solve_1(EXAMPLE_DATA) == 2


def test_day2_part2_example():
    assert day2.solve_2(EXAMPLE_DATA) == 1


def test_day2_part1(input_data):
    assert day2.solve_1(input_data) == 569


def test_day2_part2(input_data):
    assert day2.solve_2(input_data) == 346
