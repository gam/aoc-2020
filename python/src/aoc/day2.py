import re

PATTERN = r"^(\d+)-(\d+) (\w+):\s(.+)\s*$"


def _parse(line):
    return re.match(PATTERN, line).groups()


def _find_valid_passwords(data, validator):
    return [x for x in data if validator(*_parse(x))]


def _validator_1(min, max, char, password):
    return int(min) <= password.count(char) <= int(max)


def _get_characters(indices, string):
    return [string[int(i)-1] for i in indices]


def _validator_2(idx1, idx2, char, password):
    candidates = _get_characters([idx1, idx2], password)
    return sum([1 for c in candidates if c == char]) == 1


def solve(data):
    print('Part 1:', len(_find_valid_passwords(data, _validator_1)))
    print('Part 2:', len(_find_valid_passwords(data, _validator_2)))


def solve_1(data):
    return len(_find_valid_passwords(data, _validator_1))


def solve_2(data):
    return len(_find_valid_passwords(data, _validator_2))
