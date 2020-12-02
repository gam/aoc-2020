from pathlib import Path

import pytest
from aoc.aoc_utils import load_data_as_ints
import aoc.day1 as day1

EXAMPLE_DATA = [1721, 979, 366, 299, 675, 1456]
DATA_DIR = Path(__file__).parent / 'data'


@pytest.fixture()
def input_data():
    return load_data_as_ints(DATA_DIR / 'day1_data')


def test_day1_part1_example():
    """
    Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input);
    apparently, something isn't quite adding up.
    Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

    For example, suppose your expense report contained the following:

    1721
    979
    366
    299
    675
    1456
    In this list, the two entries that sum to 2020 are 1721 and 299.
    Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

    Of course, your expense report is much larger.
    Find the two entries that sum to 2020; what do you get if you multiply them together?
    """
    assert day1.solve_1(EXAMPLE_DATA) == 514579


def test_day1_part2_example():
    """
    The Elves in accounting are thankful for your help; one of them even offers you a starfish coin
    they had left over from a past vacation. They offer you a second one if you can find three numbers
    in your expense report that meet the same criteria.

    Using the above example again, the three entries that sum to 2020 are 979, 366, and 675.
    Multiplying them together produces the answer, 241861950.

    In your expense report, what is the product of the three entries that sum to 2020?
    """
    assert day1.solve_2(EXAMPLE_DATA) == 241861950


def test_day1_part1(input_data):
    assert day1.solve_1(input_data) == 840324


def test_day1_part2(input_data):
    assert day1.solve_2(input_data) == 170098110