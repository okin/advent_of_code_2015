from day1 import elevator, basement_finder

inputs = (
    ("(())", 0),
    ("()()", 0),
    ("(((", 3),
    ("(()(()(", 3),
    ("))(((((", 3),
    ("())", -1),
    ("))(", -1),
    (")))", -3),
    (")())())", -3)
)


def test_elevator():
    for example, expected in inputs:
        assert elevator(example) == expected


basement_inputs = (
    (')', 1),
    ('()())', 5)
)


def test_basement_finder():
    for example, expected in basement_inputs:
        assert basement_finder(example) == expected
