from day4 import mine_advent_coin, compute_hash


def test_computing():
    h = compute_hash('abcdef609043')
    assert h == '000001dbbfa3a5c83a2d506429c7b00e'
    assert h.startswith('00000')


def test_hashing1():
    number, first_hash = mine_advent_coin('abcdef')
    assert first_hash.startswith('000001dbbfa')
    assert number == 609043


def test_hashing2():
    number, second_hash = mine_advent_coin('pqrstuv')
    assert second_hash.startswith('000006136ef')
    assert number == 1048970

