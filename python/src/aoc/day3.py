from math import prod


def solve(map, delta_x=3, delta_y=1):
    x = trees = 0
    for row in map[::delta_y]:
        trees += 1 if row[x] == '#' else 0
        x += delta_x
        x %= len(row)
    return trees


def solve_1(map):
    return solve(map)


def solve_2(map):
    trees = [solve(map, delta_x=x) for x in [1, 3, 5, 7]]
    trees.append(solve(map, delta_x=1, delta_y=2))
    return prod(trees)
