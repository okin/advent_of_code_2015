from day2 import wrapping_paper_dimension, ribbon_length

examples = (
    ("2x3x4", 58),
    ("1x1x10", 43)
)


def test_wrapping():
    for example, expected in examples:
        assert wrapping_paper_dimension(example) == expected


ribbons = (
    ("2x3x4", 34),
    ("1x1x10", 14)
)


def test_box():
    for example, expected in ribbons:
        assert ribbon_length(example) == expected
