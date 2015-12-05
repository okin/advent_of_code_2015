from day3 import move, get_house_count, get_house_count_robosanta


def test_visited_houses():
    assert get_house_count('>') == 2
    assert get_house_count('^>v<') == 4
    assert get_house_count('^v^v^v^v^v') == 2


def test_visited_houses_with_robosanta():
    assert get_house_count_robosanta('^v') == 3
    assert get_house_count_robosanta('^>v<') == 3
    assert get_house_count_robosanta('^v^v^v^v^v') == 11


def test_moving():
    m = list(move('v'))
    assert len(m) == 2