def load_data_as_ints(filename):
    return [int(n) for n in load_data(filename)]


def load_data(filename):
    with open(filename) as f:
        return f.read().split('\n')
